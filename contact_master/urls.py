from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.fill_contact, name='fill_contact'),
    path('savecontact.do', views.save_contact, name='save_contact'),
    path('showcontacts.do', views.show_all_contacts, name='show_all_contacts')
]