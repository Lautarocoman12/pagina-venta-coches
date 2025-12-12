from django.urls import path
from .views import index, login_view, registro, dashboard

urlpatterns = [
    path("", index, name="index"),            # raíz: muestra index.html
    path("login/", login_view, name="login"),
    path("registro/", registro, name="registro"),
    path("dashboard/", dashboard, name="dashboard"),
]
