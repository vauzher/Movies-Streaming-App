from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True, default='default_photo.jpg')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
