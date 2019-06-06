from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_name = models.CharField(blank=False, max_length=50)
    profile_image = models.ImageField(upload_to='images', blank=False)
    contact_no = models.PositiveIntegerField()
    email = models.EmailField(blank=True)
    x = models.DecimalField(max_digits=9, decimal_places=6,default=0.0)
    y = models.DecimalField(max_digits=9, decimal_places=6,default=0.0)

    def __str__(self):
        return self.user_name
