""" User Views"""

# Create your views here.

#Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

#Exceptions
from django.db.utils import IntegrityError

#Models
from django.contrib.auth.models import User
from profile_user.models import Profile

# Forms
from profile_user.forms import ProfileForm

@login_required
def update_profile(request):
    """Update a user's profile view."""
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']   
            profile.biography= data['biography']
            profile.picture = data['picture']
            profile.save()


            return redirect('update_profile')
                        
    else :
        form = ProfileForm()

    return render(
        request = request,
        template_name ='users/update_profile.html',
        context = {
            'profile': profile,
            'user' : request.user,
            'form' : form
            }
        )



def login_view(request):
    """Login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
         username=username,
         password=password)
        if user :
             login(request,user)
             return redirect('feed')
        else: 
            return render(
                request,
             'users/login.html',
             {'error':'Invalid username or password'}
            )
    return render(request, 'users/login.html')

def signup(request):
    """signup view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        
        if password != password_confirmation:
            return render (
            request,
            'users/signup.html',
            {'error':'Password confirmation doesn not match'})

        try:
            user = User.objects.create_user(username=username,password=password)
        except IntegrityError:
            return render (
            request,
            'users/signup.html',
            {'error':'Username already exist, please use a different username'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect ('login')
                
    return render (request, 'users/signup.html')

@login_required
def logout_view(request):
        """logout a user."""
        logout(request) 
        return redirect('login')