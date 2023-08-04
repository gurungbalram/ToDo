from django.urls import path
from .views import *

urlpatterns = [
    path("home/", home, name='home'),
    path('create/', create_todo, name='create'),
    path('edit/<pk>', edit_todo, name='edit'),
    path('delete/<pk>', delete_todo, name='delete')
]