""" Posts URLs."""

# Django 
from django.urls import path

# Views
from posts import views


urlpatterns = [
    path(
        route='posts/',
        view = views.PostsFeedView.as_view(), 
        name = 'feed'
        ),
    path(
        route = 'posts/new/',
        view = views.create,
        name='create'
        ),
]