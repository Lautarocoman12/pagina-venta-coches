from django.urls import path
from .views import index, login_view, registro, dashboard, marketplace, publicar_producto

urlpatterns = [
    path("", index, name="index"),
    path("login/", login_view, name="login"),
    path("registro/", registro, name="registro"),
    path("dashboard/", dashboard, name="dashboard"),
    path("marketplace/", marketplace, name="marketplace"),
    path("marketplace/publicar/", publicar_producto, name="publicar_producto"),
]
