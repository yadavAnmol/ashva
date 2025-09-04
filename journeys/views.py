# Create your views here.
from django.shortcuts import render, redirect
from .models import Photo

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def journeys(request):   # 👈 this was missing
    photos = Photo.objects.all()
    return render(request, "journeys.html", {"photos": photos})

def add_photo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES.get("image")  # get uploaded image

        Photo.objects.create(
            title=title,
            description=description,
            image=image   # 👈 use 'image' instead of 'file'
        )
        return redirect("journeys")

    return render(request, "add.html")



def contact(request):
    return render(request, "contact.html")
