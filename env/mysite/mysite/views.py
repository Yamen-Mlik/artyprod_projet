from django.shortcuts import render 
from django.template import loader
def home_page(request): 
    context={'val':"Menu Acceuil"}
    return render(request,'home.html',context)