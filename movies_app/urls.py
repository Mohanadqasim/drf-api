from django.urls import path
from .views import MoviesList,MoviesDetail
# from .views import GameList,GameDetail

urlpatterns=[
    path('',MoviesList.as_view(),name='movies_list'),
    path('/<int:pk>/',MoviesDetail.as_view(),name='movie_detail')

]