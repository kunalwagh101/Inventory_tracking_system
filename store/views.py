"""
    Module name :- views
"""

from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    DetailView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from store.models import Equipment, EquipmentType, Allocation
from store.forms import (
    EquipmentTypeForm,
    AddEquipmentForm,
    UpdateEquipmentForm,
    CreateAllocationForm,
    UpdateAllocationForm,
)


# Create your views here.
class ListEquipmentType(LoginRequiredMixin, ListView):
    """
    List equipment types.
    """

    model = EquipmentType
    template_name = "store/list_equipment_type.html"
    context_object_name = "equipment_types"
    login_url = reverse_lazy("accounts:login")


class CreateEquipmentType(LoginRequiredMixin, CreateView):
    """
    Create equipment type.
    """

    model = EquipmentType
    template_name = "store/form.html"
    form_class = EquipmentTypeForm
    success_url = reverse_lazy("store:equipment-types")
    login_url = reverse_lazy("accounts:login")

    def get_context_data(self, **kwargs):
        """
        Overridden get context data.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Equipment Type"
        return context


class DeleteEquipmentType(LoginRequiredMixin, DeleteView):
    """
    Delete equipment type.
    """

    model = EquipmentType
    template_name = "store/delete.html"
    success_url = reverse_lazy("store:equipment-types")
    context_object_name = "item"
    login_url = reverse_lazy("accounts:login")

    def get_context_data(self, **kwargs):
        """
        Overriden get context data.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Equipment Type"
        return context


class ListParticularEquipments(LoginRequiredMixin, ListView):
    """
    List particular equipments.
    """

    model = Equipment
    template_name = "store/list_equipment.html"
    paginate_by = 25
    login_url = reverse_lazy("accounts:login")

    def get_queryset(self):
        """
        Overridden get queryset method.
        """
        filtering = self.kwargs["filter"]
        equipment_type = EquipmentType.objects.get(name=self.kwargs["equipment_type"])

        if filtering == "assigned":
            query = self.model.get_assigned_equipments(equipment_type=equipment_type)[
                ::-1
            ]
        elif filtering == "under_repair":
            query = self.model.get_under_repair_equipments(
                equipment_type=equipment_type
            )[::-1]
        else:
            query = self.model.get_all_functional_equipments(
                equipment_type=equipment_type
            )[::-1]

        return query

    def get_context_data(self, **kwargs):
        """
        Get Context data.
        """
        context = super().get_context_data(**kwargs)
        context["total"] = len(self.get_queryset())
        context["equipment_type"] = self.kwargs["equipment_type"]
        context["filter"] = self.kwargs["filter"]
        return context


class CreateEquipment(LoginRequiredMixin, CreateView):
    """
    Create equipment.
    """

    model = Equipment
    form_class = AddEquipmentForm
    template_name = "store/create_equipment.html"
    success_url = reverse_lazy("store:equipment-types")
    login_url = reverse_lazy("accounts:login")

    def get_context_data(self, **kwargs):
        """
        Overridden get context data method.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Equipment"
        return context


class UpdateEquipment(LoginRequiredMixin, UpdateView):
    """
    Update equipment.
    """

    model = Equipment
    template_name = "store/form.html"
    form_class = UpdateEquipmentForm
    login_url = reverse_lazy("accounts:login")

    def get_context_data(self, **kwargs):
        """
        Overridden get context data.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Equipment"
        context["equipment_type"] = self.kwargs["equipment_type"]
        return context

    def get_success_url(self):
        """
        Get success URL.
        """
        return reverse_lazy(
            "store:particular-equipments",
            kwargs={
                "equipment_type": self.kwargs["equipment_type"],
                "filter": "working",
            },
        )


class DeleteEquipment(LoginRequiredMixin, DeleteView):
    """
    Delete equipment.
    """

    model = Equipment
    template_name = "store/delete.html"
    login_url = reverse_lazy("accounts:login")

    def get_context_data(self, **kwargs):
        """
        Get Context data.
        """
        context = super().get_context_data(**kwargs)
        context["equipment_type"] = self.kwargs["equipment_type"]
        return context

    def get_success_url(self):
        """
        Get success URL.
        """
        return reverse_lazy(
            "store:particular-equipments",
            kwargs={
                "equipment_type": self.kwargs["equipment_type"],
                "filter": "working",
            },
        )


class DetailEquipment(LoginRequiredMixin, DetailView):
    """
    Detail Equipment.
    """

    login_url = reverse_lazy("accounts:login")
    model = Equipment
    template_name = "store/detail.html"
    context_object_name = "equipment"

    def get_context_data(self, **kwargs):
        """
        Get Context data.
        """
        context = super().get_context_data(**kwargs)
        context["equipment_type"] = self.kwargs["equipment_type"]
        return context


class CreateAllocation(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Create Allocation.
    """

    model = Allocation
    form_class = CreateAllocationForm
    template_name = "store/create_allocation.html"
    success_url = reverse_lazy("store:create-allocation")
    login_url = reverse_lazy("accounts:login")
    success_message = "Allocated"

    def get_context_data(self, **kwargs):
        """
        Get context data.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Allocation"
        return context


class UpdateAllocation(LoginRequiredMixin, UpdateView):
    """
    Update Allocation.
    """

    model = Allocation
    form_class = UpdateAllocationForm
    template_name = "store/form.html"
    login_url = reverse_lazy("acconts:login")
    success_url = reverse_lazy("store:allocations")

    def get_context_data(self, **kwargs):
        """
        Get context data.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Allocation"
        return context


class DeleteAllocation(LoginRequiredMixin, DeleteView):
    """
    Delete Allocation.
    """

    model = Allocation
    template_name = "store/delete.html"
    success_url = reverse_lazy("store:allocations")
    login_url = reverse_lazy("accounts:login")

    def get_context_data(self, **kwargs):
        """
        Get context data.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Allocation"
        return context


class ListAllocation(LoginRequiredMixin, ListView):
    """
    List Allocations.
    """

    model = Allocation
    template_name = "store/list_allocation.html"
    paginate_by = 25
    login_url = reverse_lazy("accounts:login")

    def get_queryset(self):
        """
        Overriding get_queryset().
        """
        return self.model.get_non_returned_allocations()[::-1]


class SearchEquipmentType(LoginRequiredMixin, ListView):
    """
    Search equipment type.
    """

    model = EquipmentType
    template_name = "store/list_equipment_type.html"
    context_object_name = "equipment_types"
    login_url = reverse_lazy("accounts:login")

    def get_queryset(self):
        """
        Overridden get queryset method.
        """
        search = self.request.GET["search"]
        return self.model.objects.filter(name__icontains=search)


class SearchEquipment(LoginRequiredMixin, ListView):
    """
    Search equipment.
    """

    model = Equipment
    template_name = "store/list_equipment.html"
    context_object_name = "equipments"
    paginate_by = 25
    login_url = reverse_lazy('accounts"login')

    def get_queryset(self):
        """
        Overridden get queryset method.
        """
        search = self.request.GET["search"]
        equipment_type = EquipmentType.objects.get(name=self.kwargs["equipment_type"])

        query = self.model.get_all_functional_equipments(equipment_type=equipment_type)

        return query.filter(
            Q(label__icontains=search)
            | Q(equipment_type__name__icontains=search)
            | Q(buy_date__icontains=search)
            | Q(serial_number__icontains=search)
            | Q(model_number__icontains=search)
            | Q(price__icontains=search)
            | Q(brand__icontains=search)
        )[::-1]

    def get_context_data(self, **kwargs):
        """
        Get Context data.
        """
        context = super().get_context_data(**kwargs)
        context["total"] = len(self.get_queryset())
        context["equipment_type"] = self.kwargs["equipment_type"]
        context["search"] = self.request.GET["search"]
        return context


class SearchAllocation(LoginRequiredMixin, ListView):
    """
    Search equipment type.
    """

    model = Allocation
    template_name = "store/list_allocation.html"
    paginate_by = 25
    login_url = reverse_lazy("accounts:login")

    def get_queryset(self):
        """
        Overridden get queryset method.
        """
        search = self.request.GET["search"]
        query = self.model.get_non_returned_allocations()
        return query.filter(
            Q(user__username__icontains=search) | Q(equipment__label__icontains=search)
        )

    def get_context_data(self, **kwargs):
        """
        Overriding get_context_data().
        """
        context = super().get_context_data(**kwargs)
        context["search"] = self.request.GET["search"]
        return context


def get_ids(request):
    """
    Get ids.
    """
    equipments = Equipment.get_ids(request.GET["equipment_type"])
    return JsonResponse(list(equipments), safe=False)


def get_label(request):
    """
    Get Label.
    """
    equipment = Equipment.objects.filter(equipment_type=request.GET["equipment_type"])[
        0
    ]
    return JsonResponse(equipment.set_label, safe=False)
