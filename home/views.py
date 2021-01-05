from django.shortcuts import render, redirect
from .models import contact
# Create your views here.

def index(request):
    return render(request,"home.html")

def contact_form(request):
    if request.method=="POST":
        message=request.POST["message"]
        email=request.POST["email"]
        name=request.POST["display_name"]
        q=contact(message=message,email=email,name=name)
        q.save()
        return redirect("/")

    else:
        return render(request,"contact.html")

