from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from .models import Movie, Genre
from user_interactions.models import UserList, Rating, Like, Comment
from django.db.models import F, Count
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.apps import AppConfig

class HomeView(ListView):
    model = Movie
    template_name = 'home.html'
    context_object_name = 'movies'

    @staticmethod
    def get_recommended_movies(user):
        if not user.is_authenticated:
            return Movie.objects.none()
        
        liked_movies = Movie.objects.filter(like__user=user)
        listed_movies = Movie.objects.filter(user_lists__user=user)
        
        user_genres = set()
        for movie in (liked_movies | listed_movies).distinct():
            user_genres.update(movie.genres.all())
        
        recommended_movies = Movie.objects.filter(genres__in=user_genres).exclude(
            id__in=(liked_movies | listed_movies)
        ).distinct().order_by('-views')[:10]
        
        return recommended_movies

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movies = Movie.objects.all()
        for movie in movies:
            movie.like_count = movie.get_like_count()
            movie.average_rating = movie.get_average_rating()
        context['movies'] = movies
        trending_movies = get_trending_movies()
        for movie in trending_movies:
            movie.like_count = movie.get_like_count()
            movie.average_rating = movie.get_average_rating()
        context['trending_movies'] = trending_movies
        
        # Add recommended movies to the context
        recommended_movies = self.get_recommended_movies(self.request.user)
        for movie in recommended_movies:
            movie.like_count = movie.get_like_count()
            movie.average_rating = movie.get_average_rating()
        context['recommended_movies'] = recommended_movies
        
        return context

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = self.object
        movie.like_count = movie.get_like_count()
        movie.average_rating = movie.get_average_rating()
        movie.comments = movie.get_comments()
        related_movies = self.get_related_movies(movie)
        context['related_movies'] = related_movies
        user = self.request.user
        if user.is_authenticated:
            # Check if the movie is in any of the user's lists
            context['in_user_list'] = UserList.objects.filter(user=user, movies=movie).exists()
            
            # Get user's rating for this movie
            try:
                user_rating = Rating.objects.get(user=user, movie=movie)
                context['user_rating'] = user_rating.value
            except Rating.DoesNotExist:
                context['user_rating'] = None

            # Check if user has liked this movie
            context['user_liked'] = Like.objects.filter(user=user, movie=movie).exists()

            # Get user's comment for this movie, if any (changed from get to filter().first())
            user_comment = Comment.objects.filter(user=user, movie=movie).first()
            context['user_comment'] = user_comment.content if user_comment else None

        return context

    def get_related_movies(self, movie):
        genres = movie.genres.all()
        related_movies = Movie.objects.filter(genres__in=genres).exclude(id=movie.id).distinct()[:5]
        for related_movie in related_movies:
            related_movie.like_count = related_movie.get_like_count()
            related_movie.average_rating = related_movie.get_average_rating()
        return related_movies

def get_trending_movies():
    one_week_ago = timezone.now() - timedelta(days=100)
    trending_movies = Movie.objects.filter(views__gt=1000, created_at__gte=one_week_ago).order_by('-views')[:10]
    return trending_movies


class MoviesView(ListView):
    model = Movie
    template_name = 'movies.html'
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movies = Movie.objects.all()
        for movie in movies:
            movie.like_count = movie.get_like_count()
            movie.average_rating = movie.get_average_rating()
        context['movies'] = movies
        context['genres'] = Genre.objects.all()
        
        # Featured movies for the slider (using the top 3 trending movies)
        featured_movies = self.get_featured_movies()
        print(f"Number of featured movies: {len(featured_movies)}")  # Debug print
        for movie in featured_movies:
            movie.like_count = movie.get_like_count()
            movie.average_rating = movie.get_average_rating()
            print(f"Featured movie: {movie.title}, Views: {movie.views}")  # Debug print
        context['featured_movies'] = featured_movies
        
        return context

    def get_featured_movies(self):
        # Get top 3 most viewed movies
        featured_movies = Movie.objects.order_by('-views')[:3]
        return featured_movies

    def get_trending_movies(self):
        one_week_ago = timezone.now() - timedelta(days=14)
        trending_movies = Movie.objects.filter(views__gt=1000, created_at__gte=one_week_ago).order_by('-views')[:10]
        return trending_movies  
    

