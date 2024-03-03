"""
    Module name :- forms
"""

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    """
    Login Form.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializer.
        """
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class SignUpForm(UserCreationForm):
    """
    Sign Up Form.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializer.
        """
        super().__init__(*args, **kwargs)

        for key, field in self.fields.items():
            if key == "admin":
                continue
            field.widget.attrs["class"] = "form-control"

    class Meta:
        """
        Meta class
        """

        model = User
        fields = ("username", "email", "first_name", "last_name")

    admin = forms.BooleanField(required=False)

    def save(self, commit=True):
        """
        Overriding save method.
        """
        form = super().save(commit=False)
        is_true = self.cleaned_data["admin"]

        form.is_staff = is_true
        form.is_superuser = is_true

        if commit:
            form.save()
        return form


class UpdateUserForm(forms.ModelForm):
    """
    Update User Form.
    """

    class Meta:
        """
        Meta class for Update User Form.
        """

        model = User
        fields = ("username", "email", "first_name", "last_name")

    def __init__(self, *args, **kwargs):
        """
        Overriding __init__ method.
        """
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
