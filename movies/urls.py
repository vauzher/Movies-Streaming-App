from django.urls import path
from .views import HomeView, MovieDetailView, TrendingMoviesView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('trending/', TrendingMoviesView.as_view(), name='trending'),
]