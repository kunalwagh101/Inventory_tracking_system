"""
    Module name :- urls
"""

from django.urls import path
from store.views import (
    ListEquipmentType,
    CreateEquipmentType,
    DeleteEquipmentType,
    CreateEquipment,
    UpdateEquipment,
    DeleteEquipment,
    DetailEquipment,
    ListParticularEquipments,
    CreateAllocation,
    UpdateAllocation,
    DeleteAllocation,
    ListAllocation,
    SearchEquipment,
    SearchEquipmentType,
    SearchAllocation,
    get_ids,
    get_label,
)

app_name = "store"

urlpatterns = [
    path("", ListEquipmentType.as_view(), name="equipment-types"),
    path(
        "add-equipment-type/", CreateEquipmentType.as_view(), name="add-equipment-type"
    ),
    path(
        "delete-equipment-type/<int:pk>/",
        DeleteEquipmentType.as_view(),
        name="delete-equipment-type",
    ),
    path("add-equipment/", CreateEquipment.as_view(), name="add-equipment"),
    path(
        "update-equipment/<str:equipment_type>/<int:pk>/",
        UpdateEquipment.as_view(),
        name="update-equipment",
    ),
    path(
        "delete-equipment/<str:equipment_type>/<int:pk>/",
        DeleteEquipment.as_view(),
        name="delete-equipment",
    ),
    path(
        "detail-equipment/<str:equipment_type>/<int:pk>/",
        DetailEquipment.as_view(),
        name="detail-equipment",
    ),
    path(
        "equipments/<str:equipment_type>/<str:filter>/",
        ListParticularEquipments.as_view(),
        name="particular-equipments",
    ),
    path("create-allocation/", CreateAllocation.as_view(), name="create-allocation"),
    path(
        "allocations/update-allocation/<int:pk>",
        UpdateAllocation.as_view(),
        name="update-allocation",
    ),
    path(
        "allocations/delete-allocation/<int:pk>",
        DeleteAllocation.as_view(),
        name="delete-allocation",
    ),
    path("allocations/", ListAllocation.as_view(), name="allocations"),
    path(
        "search-equipment/<str:equipment_type>/",
        SearchEquipment.as_view(),
        name="search-equipment",
    ),
    path(
        "search-equipment-type/",
        SearchEquipmentType.as_view(),
        name="search-equipment-type",
    ),
    path("search-allocation/", SearchAllocation.as_view(), name="search-allocation"),
    path("get_ids/", get_ids, name="get_ids"),
    path("get_label/", get_label, name="get_label"),
]
