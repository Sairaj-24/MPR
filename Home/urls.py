from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',view_home),
    path('book-free-class/',free_class_form_view, name='book_free_class'),
     path('book-one-to-one-class/',one_to_one_class_form_view, name='book_one_to_one_class'),
]