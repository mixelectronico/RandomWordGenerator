from django.urls import path, include
from . import views

urlpatterns = [
    path('random_word/', views.random_word, name="random_word"),
    path('random_word/reset/', views.reset, name="reset"),
]