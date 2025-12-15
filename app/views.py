from django.shortcuts import render, redirect, get_object_or_404
from .models import Coche, FotoCoche
from .forms import CocheForm


# ----------------------
# PÁGINAS BÁSICAS
# ----------------------

def index(request):
    return render(request, "index.html")


def login_view(request):
    return render(request, "login.html")


def registro(request):
    return render(request, "register.html")


def dashboard(request):
    return render(request, "dashboard.html")

def comovender(request):
    return render(request, "comovender.html")


# ----------------------
# MARKETPLACE + FILTROS
# ----------------------

def marketplace(request):
    productos = Coche.objects.all().order_by("-fecha_publicacion")

    # Filtros por categoría (sidebar)
    combustible = request.GET.get("combustible")
    transmision = request.GET.get("transmision")

    if combustible:
        productos = productos.filter(combustible=combustible)

    if transmision:
        productos = productos.filter(transmision=transmision)

    return render(request, "marketplace.html", {
        "productos": productos
    })


# ----------------------
# PUBLICAR PRODUCTO
# ----------------------

def publicar_producto(request):
    if request.method == "POST":
        form = CocheForm(request.POST)
        fotos = request.FILES.getlist("fotos")

        if form.is_valid():
            coche = form.save()

            # Guardar múltiples fotos
            for foto in fotos:
                FotoCoche.objects.create(
                    coche=coche,
                    imagen=foto
                )

            return redirect("marketplace")
    else:
        form = CocheForm()

    return render(request, "publicar_producto.html", {
        "form": form
    })


# ----------------------
# DETALLE DEL PRODUCTO
# ----------------------

def detalle_producto(request, pk):
    producto = get_object_or_404(Coche, pk=pk)
    return render(request, "detalle_producto.html", {
        "producto": producto
    })

