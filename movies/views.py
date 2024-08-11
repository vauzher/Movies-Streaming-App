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
        context['trending_movies'] = get_trending_movies()
        return context


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    context_object_name = 'movie'

class TrendingMoviesView(ListView):
    model = Movie
    template_name = 'trending.html'
    context_object_name = 'trending_movies'

    def get_queryset(self):
        return Movie.objects.order_by('-average_rating')[:10]


def get_trending_movies():
    one_week_ago = timezone.now() - timedelta(days=7)
    trending_movies = Movie.objects.filter(views__gt=1000, created_at__gte=one_week_ago).order_by('-views', '-likes')[:10]
    return trending_movies

def trending_movies_view(request):
    trending_movies = get_trending_movies()
    return render(request, 'trending_movies.html', {'trending_movies': trending_movies})
