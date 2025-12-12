from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def login_view(request):
    return render(request, "login.html")

def registro(request):
    return render(request, "register.html")

def dashboard(request):
    return render(request, "dashboard.html")
