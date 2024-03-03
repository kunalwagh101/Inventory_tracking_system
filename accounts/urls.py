"""
    Module name :- urls
"""

from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView
from accounts.views import (
    CreateUser,
    UserLoginView,
    UpdateUser,
    ListUser,
    DeleteUser,
    SearchUser,
)


app_name = "accounts"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path(
        "logout/",
        LogoutView.as_view(next_page=reverse_lazy("accounts:login")),
        name="logout",
    ),
    path("users/", ListUser.as_view(), name="users"),
    path("add-user/", CreateUser.as_view(), name="add-user"),
    path("update-user/<int:pk>/", UpdateUser.as_view(), name="update-user"),
    path("delete-user/<int:pk>/", DeleteUser.as_view(), name="delete-user"),
    path("search-user/", SearchUser.as_view(), name="search-user"),
]
