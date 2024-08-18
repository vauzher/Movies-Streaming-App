from django.urls import path
from .views import HomeView, MovieDetailView, MoviesView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movies/', MoviesView.as_view(), name='movies_page'),
]
