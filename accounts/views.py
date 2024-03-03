"""
    Module name :- views
"""

from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from accounts.forms import SignUpForm, LoginForm, UpdateUserForm

# Create your views here.


class CreateUser(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    """
    Create user.
    """

    template_name = "accounts/user.html"
    form_class = SignUpForm
    success_url = reverse_lazy("accounts:users")
    permission_required = ["is_superuser"]
    login_url = reverse_lazy("accounts:login")

    def form_invalid(self, form):
        """
        Invalid form.
        """
        messages.info(self.request, form.errors)
        return super().form_invalid(form)


class UpdateUser(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    """
    Update user.
    """

    model = User
    form_class = UpdateUserForm
    template_name = "accounts/user.html"
    context_object_name = "user"
    success_url = reverse_lazy("accounts:users")
    login_url = reverse_lazy("accounts:login")

    def form_invalid(self, form):
        """
        Invalid form.
        """
        messages.info(self.request, form.errors)
        return super().form_invalid(form)

    def has_permission(self) -> bool:
        """
        Method to check permissions.
        """
        return self.request.user.is_superuser or (
            self.get_object() == self.request.user
        )


class DeleteUser(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    """
    Delete user.
    """

    model = User
    template_name = "accounts/delete.html"
    success_url = reverse_lazy("accounts:users")
    context_object_name = "user"
    login_url = reverse_lazy("accounts:login")

    def has_permission(self) -> bool:
        """
        Method to check permissions.
        """
        return self.request.user.is_superuser or (
            self.get_object() == self.request.user
        )

    def get_context_data(self, **kwargs):
        """
        Overriding get context data method.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete User"
        return context


class ListUser(LoginRequiredMixin, ListView):
    """
    List all users.
    """

    model = User
    template_name = "accounts/list_user.html"
    paginate_by = 25
    login_url = reverse_lazy("accounts:login")


class UserLoginView(LoginView):
    """
    Login View.
    """

    template_name = "accounts/login.html"
    form_class = LoginForm
    next_page = reverse_lazy("store:equipment-types")


class SearchUser(LoginRequiredMixin, ListView):
    """
    Search User.
    """

    model = User
    template_name = "accounts/list_user.html"
    paginate_by = 25
    login_url = reverse_lazy("accounts:login")

    def get_queryset(self):
        """
        Overriding get queryset.
        """
        search = self.request.GET["search"]
        return self.model.objects.filter(
            Q(username__icontains=search)
            | Q(first_name__icontains=search)
            | Q(last_name__icontains=search)
        )
