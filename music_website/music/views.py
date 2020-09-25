from django.shortcuts import render
from .models import Genre
from user.models import AdditionalArtistDetail

def discover(request):
    genres = Genre.objects.all()
    artists = AdditionalArtistDetail.objects.all()

    return render(request, 'music/discover.html', {'genres' : genres, 'artists' : artists})