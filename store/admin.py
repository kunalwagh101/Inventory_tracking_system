"""
    Module name :- admin
"""

from django.contrib import admin
from store.models import Equipment, EquipmentType, Allocation


# Register your models here.
@admin.register(EquipmentType)
class EquipmentTypeAdmin(admin.ModelAdmin):
    """
    Equipment Type admin class.
    """

    verbose_name = "Equipment Type"


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    """
    Equipment admin class.
    """

    list_display = ["label", "equipment_type", "under_repair", "functional"]


@admin.register(Allocation)
class AllocationAdmin(admin.ModelAdmin):
    """
    Allocation admin class.
    """

    list_display = ["user", "equipment", "returned"]
