from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit', views.edit, name='edit'),
    path('addExperience', views.addExperience, name='addExperience'),
    path('addQualification', views.addQualification, name='addQualification')
]