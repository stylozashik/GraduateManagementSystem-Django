from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add/',views.add_student),
    path('about/',views.about),
    ]