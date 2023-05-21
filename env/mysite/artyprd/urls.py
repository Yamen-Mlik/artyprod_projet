from django.urls import path   #,include
from . import views

urlpatterns = [	
    path('equipe/', views.equipe, name='equipe'),
    path('contact/', views.contact, name='contact'),
    path('register/',views.register, name = 'register'),
    path('', views.portfolio, name='portfolio'),
    path('detail/<int:projet_id>/', views.detail, name='detail'),
    path('projet/create/', views.projet_create, name='projet_create'),
    path('projet/<int:projet_id>/update/',views.projet_update, name='projet_update'),
    path('projet/<int:projet_id>/delete/', views.projet_delete, name='projet_delete'),
    path('create/', views.personnel_create, name='personnel_create'),
    path('update/<int:pk>/', views.personnel_update, name='personnel_update'),
    path('delete/<int:pk>/', views.personnel_delete, name='personnel_delete'),
    path('demande/', views.demande_service, name='demande_service'),
    path('demande/confirmation/', views.demande_confirmation, name='demande_confirmation'),
     path('demandes/', views.service_demande_list, name='service_demande_list'),
    ]
