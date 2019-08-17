""" Posts models."""

#Django
from django.db import models 
from django.contrib.auth.models import User

class Posts(models.Model):
    """ Posts model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('profile_user.Profile', on_delete=models.CASCADE)
    

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """Return title and username"""
        return '{} by @{}'.format(self.title, self.user.username)
    