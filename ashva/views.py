from django.shortcuts import render

def home(request):
    return render(request, "index.html")
    # return render(request, "index.html", {})

def about(request):
    return render(request, "about.html")

def add(request):
    return render(request, "add.html")

def contact(request):
    return render(request, "contact.html")

def journeys(request):
    return render(request, "journeys.html")
