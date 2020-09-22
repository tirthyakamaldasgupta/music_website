from django.db import models
from django.contrib.auth.models import User

class AdditionalListenerDetail(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

class AdditionalArtistDetail(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)