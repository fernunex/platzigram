"""Users URLs."""

# Django 
from django.urls import path
from django.views.generic import TemplateView
# Views
from profile_user import views


urlpatterns = [

    # Posts
    path(
        route= '<str:username>/',
        view = TemplateView.as_view(template_name = 'users/detail.html'),
        name = 'detail'
    ),



    # Managment
    path(
        route='users/login/', 
        view = views.login_view, 
        name = 'login' 
    ),
    path(
        route='users/logout/', 
        view = views.logout_view, 
        name = 'logout' 
    ),
    path(
        route='users/signup/', 
        view = views.signup, 
        name = 'signup' 
    ),
    path(
        route='users/me/profile', 
        view = views.update_profile, 
        name = 'update_profile' 
    ),
]