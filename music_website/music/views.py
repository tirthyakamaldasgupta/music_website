from django.shortcuts import render
from .models import Genre, Language
from user.models import AdditionalArtistDetail

def discover(request):
    genres = Genre.objects.all()
    artists = AdditionalArtistDetail.objects.all()
    languages = Language.objects.all()

    return render(request, 'music/discover.html', {'genres' : genres, 'artists' : artists, 'languages' : languages})