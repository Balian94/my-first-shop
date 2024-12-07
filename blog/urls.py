from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Головна сторінка з відображенням постів
    path('post/<int:pk>', views.post_detail, name='post_detail'),
]