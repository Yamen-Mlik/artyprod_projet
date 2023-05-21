from django.shortcuts import render

from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import PersonnelForm, ProjetForm, ServiceDemandeForm, UserRegistrationForm
from artyprd.forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import Personnel, Projet, Service
@login_required


def detail(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    context = {'projet': projet}
    return render(request,'artyprod/detail.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send email
        subject = 'Contact Form Submission'
        body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])

        return render(request,'artyprod/contact_success.html')

    return render(request,'artyprod/contact.html')

def equipe(request):
    members = Personnel.objects.all()
    context = {'members': members}
    return render(request,'artyprod/equipe.html', context)
def portfolio(request):
    projets = Projet.objects.all()
    context = {'projets': projets}
    return render(request, 'artyprod/portfolio.html', context)
def register(request):
    if request.method == 'POST' :
      form = UserRegistrationForm(request.POST)
      if form.is_valid():
       form.save()
       username = form.cleaned_data.get('username')
       password = form.cleaned_data.get('password1')
       user = authenticate(username=username, password=password)
    
      login(request,user)
      messages.success(request,f'Coucou {username}, Votre compte a été créé avec succès !')
      return redirect('login')
    else :
     form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form' : form})
def projet_create(request):
    if request.method == 'POST':
        form = ProjetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
    else:
        form = ProjetForm()
    return render(request,'artyprod/projet_create.html', {'form': form})

def projet_update(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    if request.method == 'POST':
        form = ProjetForm(request.POST, instance=projet)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
    else:
        form = ProjetForm(instance=projet)
    return render(request,'artyprod/projet_update.html', {'form': form, 'projet': projet})

def projet_delete(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    if request.method == 'POST':
        projet.delete()
        return redirect('portfolio')
    return render(request,'artyprod/projet_delete.html', {'projet': projet})

#pour les personel
def personnel_create(request):
    if request.method == 'POST':
        form = PersonnelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipe')
    else:
        form = PersonnelForm()
    return render(request,'artyprod/personnel_create.html', {'form': form})
def personnel_update(request, pk):
    personnel = get_object_or_404(Personnel, pk=pk)
    if request.method == 'POST':
        form = PersonnelForm(request.POST, instance=personnel)
        if form.is_valid():
            form.save()
            return redirect('equipe')
    else:
        form = PersonnelForm(instance=personnel)
    return render(request,'artyprod/personnel_update.html', {'form': form})

def personnel_delete(request, pk):
    personnel = get_object_or_404(Personnel, pk=pk)
    if request.method == 'POST':
        personnel.delete()
        return redirect('equipe')
    return render(request,'artyprod/personnel_delete.html', {'personnel': personnel})
@login_required
def demande_service(request):
    if request.method == 'POST':
        form = ServiceDemandeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('demande_confirmation')
    else:
        form = ServiceDemandeForm()
    
    context = {
        'form': form
    }
    return render(request,'artyprod/demande_service.html', context)

def demande_confirmation(request):
    return render(request,'artyprod/demande_confirmation.html')
def service_demande_list(request):
    demandes =  Service.objects.all()
    context = {
        'demandes': demandes
    }
    return render(request, 'artyprod/service_demande_list.html', context)
