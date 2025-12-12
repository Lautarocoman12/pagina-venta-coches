from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.urls")),             # conecta la app
    path("accounts/", include("allauth.urls")),  # registro + login con Google
]
