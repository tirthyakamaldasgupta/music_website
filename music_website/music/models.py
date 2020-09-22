from django.db import models
from django.conf import settings

class RecordLabel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, null=False, max_length=255)

class Genre(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, null=False, max_length=255)

class Album(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, null=False, max_length=255)
    recordlabel_id = models.ForeignKey(RecordLabel, null=False, on_delete=models.CASCADE)

class Song(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, null=False, max_length=255)
    genre_id = models.ForeignKey(Genre, null=False, on_delete=models.CASCADE)
    album_id = models.ForeignKey(Album, null=False, on_delete=models.CASCADE)
    datetime = models.DateTimeField(null=False)

class Continent(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, null=False, max_length=255)

class Country(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, null=False, max_length=255)
    continent_id = models.ForeignKey(Continent, null=False, on_delete=models.CASCADE)

class State(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, null=False, max_length=255)
    country_id = models.ForeignKey(Country, null=False, on_delete=models.CASCADE)

class District(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, null=False, max_length=255)
    continent_id = models.ForeignKey(State, null=False, on_delete=models.CASCADE)

class Venue(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, null=False, max_length=255)
    districtorcity_id = models.ForeignKey(District, null=False, on_delete=models.CASCADE)
    pincode = models.IntegerField(null=False)
    website = models.CharField(null=False, max_length=255)

class Number(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.IntegerField(null=False)
    venue_id = models.ForeignKey(Venue, null=False, on_delete=models.CASCADE)