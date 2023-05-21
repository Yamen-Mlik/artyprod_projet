from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Personnel, Projet, Service
class UserRegistrationForm(UserCreationForm):
 first_name = forms.CharField(label='Prénom')
 last_name = forms.CharField(label='Nom')
 email = forms.EmailField(label='Adresse e-mail')
 
class Meta(UserCreationForm.Meta):
 model = User
 fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')
 from .models import Projet

class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = '__all__'
class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = '__all__'
class ServiceDemandeForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['type', 'description', 'Img']