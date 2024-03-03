"""
    Module name :- forms
"""

from django import forms
from django.contrib.auth.models import User
from store.models import Equipment, EquipmentType, Allocation


class EquipmentTypeForm(forms.ModelForm):
    """
    Form for equipment type.
    """

    class Meta:
        """
        Meta class for equipment type form.
        """

        model = EquipmentType
        fields = ("name",)

        widgets = {"name": forms.TextInput(attrs={"class": "form-control"})}


class EquipmentForm(forms.ModelForm):
    """
    Equipment Form.
    """

    equipment_type = forms.ModelChoiceField(
        queryset=EquipmentType.objects.all(), empty_label="Choose Equipment Type"
    )

    class Meta:
        """
        Meta class for Equipment Form.
        """

        model = Equipment
        fields = (
            "label",
            "serial_number",
            "model_number",
            "price",
            "buy_date",
            "brand",
            "equipment_type",
        )

        widgets = {
            "label": forms.TextInput(attrs={"class": "form-control", "readonly": True}),
            "serial_number": forms.TextInput(attrs={"class": "form-control"}),
            "model_number": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "buy_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "brand": forms.TextInput(attrs={"class": "form-control"}),
        }

    equipment_type.widget.attrs.update({"class": "form-select"})


class AddEquipmentForm(EquipmentForm):
    """
    Form for equipment
    """

    def save(self, commit=True):
        """
        Overriding save().
        """
        instance = super().save(commit=False)
        instance.label = instance.set_label

        if commit:
            instance.save()
        return instance


class UpdateEquipmentForm(EquipmentForm):
    """
    Update form for equipment.
    """

    class Meta(EquipmentForm.Meta):
        """
        Meta class for Update Equipment Form.
        """

        fields = ("label",) + EquipmentForm.Meta.fields + ("under_repair", "functional")

        widgets = {
            "label": forms.TextInput(
                attrs={"class": "form-control", "readonly": "True"}
            ),
            "serial_number": forms.TextInput(attrs={"class": "form-control"}),
            "model_number": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "buy_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "brand": forms.TextInput(attrs={"class": "form-control"}),
        }

    def save(self, commit=True):
        """
        Save Method.
        """
        instance = super().save(commit=False)
        if instance.under_repair is True or instance.functional is False:
            equipment = Equipment.objects.get(pk=instance.pk)
            allocations = Allocation.objects.filter(equipment=equipment)[::-1]

            if allocations:
                last_allocation = allocations[0]
                last_allocation.returned = True
                last_allocation.save()

        if commit:
            instance.save()
        return instance


class AllocationForm(forms.ModelForm):
    """
    Allocation Form.
    """

    user = forms.ModelChoiceField(
        queryset=User.objects.all(), empty_label="Choose User"
    )

    class Meta:
        """
        Meta class.
        """

        model = Allocation
        fields = ("user", "equipment")

        widgets = {"equipment": forms.Select(attrs={"class": "form-select"})}

    user.widget.attrs.update({"class": "form-select"})


class CreateAllocationForm(AllocationForm):
    """
    Create Allocation Form.
    """

    equipment_type = forms.ModelChoiceField(
        queryset=EquipmentType.objects.all(), empty_label="Choose Equipment Type"
    )
    equipment_type.widget.attrs.update({"class": "form-select"})


class UpdateAllocationForm(AllocationForm):
    """
    Update Allocation Form.
    """

    class Meta(AllocationForm.Meta):
        """
        Meta class for Allocation Form.
        """

        fields = AllocationForm.Meta.fields + ("returned",)
