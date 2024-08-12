#TODO: Added Rating and Likes on the home page that are directly connected to the user interactions, 
#TODO: i should edit Movie_detail page to include user interactions like Rating and comments and likes...


from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from .models import Movie
from django.db.models import F
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render


class HomeView(ListView):
    model = Movie
    template_name = 'home.html'
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get all movies
        movies = Movie.objects.all()

        # Add like count and average rating to each movie
        for movie in movies:
            movie.like_count = movie.get_like_count()
            movie.average_rating = movie.get_average_rating()

        # Set movies in context
        context['movies'] = movies

        # Get trending movies
        trending_movies = get_trending_movies()

        # Add like count and average rating to each trending movie
        for movie in trending_movies:
            movie.like_count = movie.get_like_count()
            movie.average_rating = movie.get_average_rating()

        # Set trending movies in context
        context['trending_movies'] = trending_movies



        return context
    
  


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = self.object
        # Add like count and average rating to the movie
        movie.like_count = movie.get_like_count()
        movie.average_rating = movie.get_average_rating()
        movie.comments = movie.get_comments()
        # Get related movies
        related_movies = self.get_related_movies(movie)
        context['related_movies'] = related_movies

        return context

    def get_related_movies(self, movie):
        # Get the genres of the current movie
        genres = movie.genres.all()
        
        # Query for movies that share at least one genre with the current movie
        related_movies = Movie.objects.filter(genres__in=genres).exclude(id=movie.id).distinct()
        
        # Limit the number of related movies (e.g., to 5)
        related_movies = related_movies[:5]
        
        # Manually add like count and average rating to each related movie
        for related_movie in related_movies:
            related_movie.like_count = related_movie.get_like_count()
            related_movie.average_rating = related_movie.get_average_rating()
        
        return related_movies




def get_trending_movies():
    one_week_ago = timezone.now() - timedelta(days=7)
    trending_movies = Movie.objects.filter(views__gt=1000, created_at__gte=one_week_ago).order_by('-views')[:10]
    return trending_movies

