from django.urls import path
from .views import index, login_view, registro, dashboard, marketplace

urlpatterns = [
    path("", index, name="index"),
    path("login/", login_view, name="login"),
    path("registro/", registro, name="registro"),
    path("dashboard/", dashboard, name="dashboard"),
    path("marketplace/", marketplace, name="marketplace"),
]
