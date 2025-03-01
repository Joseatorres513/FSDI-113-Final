from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")  # Renders homepage

def about(request):
    return render(request, "pages/about.html")  # Renders about page