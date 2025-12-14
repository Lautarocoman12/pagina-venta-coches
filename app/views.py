from django.shortcuts import render, redirect
from .forms import CocheForm
from .models import Coche


def index(request):
    return render(request, "index.html")


def login_view(request):
    return render(request, "login.html")


def registro(request):
    return render(request, "register.html")


def dashboard(request):
    return render(request, "dashboard.html")


def marketplace(request):
    productos = Coche.objects.all().order_by("-fecha_publicacion")
    return render(request, "marketplace.html", {"productos": productos})


def publicar_producto(request):
    if request.method == "POST":
        form = CocheForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("marketplace")
    else:
        form = CocheForm()

    return render(request, "publicar_producto.html", {"form": form})



def detalle_producto(request, pk):
    producto = Coche.objects.get(pk=pk)
    return render(request, "detalle_producto.html", {"producto": producto})


from .models import Coche, FotoCoche
from .forms import CocheForm

def publicar_producto(request):
    if request.method == "POST":
        form = CocheForm(request.POST)
        fotos = request.FILES.getlist("fotos")

        if form.is_valid():
            coche = form.save()

            for foto in fotos:
                FotoCoche.objects.create(
                    coche=coche,
                    imagen=foto
                )

            return redirect("marketplace")

    else:
        form = CocheForm()

    return render(request, "publicar_producto.html", {"form": form})
