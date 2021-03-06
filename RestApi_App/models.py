from django.db import models

#######################
# for token
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.
DESCRIPTION = (
        (0, "Sunny"),
        (1, "Rainy"),
        (2, "Cloudy"),
        (3, "Snow"),
        (5, "Freezing"),
        (6, "Broken clouds")
)

class weather(models.Model):
    City = models.CharField(max_length=100)
    Temperature = models.IntegerField(default=0)
    Description = models.IntegerField(choices=DESCRIPTION, default=0)
    Icon = models.ImageField(upload_to='icon_pics', null=True, blank=True)
    Country = models.CharField(max_length=100)
    Wind = models.IntegerField(default=0)

    def __str__(self):
        return str(self.City)



# This code is triggered whenever a new user has been created and save the Token to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        