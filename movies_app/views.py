from django.shortcuts import render
from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
# Create your views here.
class MoviesList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MoviesDetail(generics.RetrieveUpdateDestroyAPIView): #RetrieveAPIView, RetrieveUpdateAPIView
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer