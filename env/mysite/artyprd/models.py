from django.db import models
from django.db import models
from datetime import date
from pyexpat import model
from django.apps import AppConfig
from django.conf import settings
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
# Create your models here.
class Personnel(models.Model):
    nom = models.CharField(max_length=255)
    skill = models.TextField(blank=True)
    ficher= models.FileField(upload_to='media/', blank=True)
    Img = models.ImageField(upload_to='media/', blank=True)
    lien_linkedIn = models.URLField(blank=True)

    def _str_(self):
        return (self.nom+","+self.lien_linkedIn)
    
class Projet(models.Model):
    libelle = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField()
    acheve = models.BooleanField(default=False)
    equipe = models.ForeignKey('Equipe', on_delete=models.PROTECT)
    Img = models.ImageField(upload_to='media/', null=True, blank=True)


    def _str_(self):
        return (self.libelle +","+self.description+","+self.date_debut+","+self.date_fin+","+self.acheve)

class Service(models.Model):
    TYPE_CHOICES = (
        ('Product Design', 'Product Design'),
        ('UX UI Design','UX UI Design'),
        ('Branding','Branding'),
        ('Digital Strategy','Digital Strategy'),
    )
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    description = models.TextField()
    Img = models.ImageField(upload_to='media/', null=True, blank=True)


    def _str_(self):
        return (self.type+","+self.description)

class Detail(models.Model):
    fichier = models.FileField(upload_to='media/')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    Projet = models.ForeignKey(Projet, on_delete=models.CASCADE , default=1)
    def _str_(self):
        return (self.fichier+","+self.service+","+self.Projet)

class Equipe(models.Model):
    nom = models.CharField(max_length=255)
    membres = models.ManyToManyField(Personnel)
    Img = models.ImageField(upload_to='media/', null=True, blank=True)


    def _str_(self):
        return (self.nom+","+self.membres)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def __str__(self):
        return self.user.username
