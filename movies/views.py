from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from .models import Movie

class HomeView(ListView):
    model = Movie
    template_name = 'home.html'
    context_object_name = 'movies'

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            movies = context['movies']
            data = {
                'movies': [
                    {
                        'id': movie.id,
                        'title': movie.title,
                        'description': movie.description,
                        'thumbnail': movie.thumbnail.url if movie.thumbnail else None,
                    } for movie in movies
                ]
            }
            return JsonResponse(data)
        return super().render_to_response(context, **response_kwargs)

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    context_object_name = 'movie'

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            movie = context['movie']
            data = {
                'id': movie.id,
                'title': movie.title,
                'description': movie.description,
                'thumbnail': movie.thumbnail.url if movie.thumbnail else None,
                'release_date': movie.release_date.isoformat(),
                'genres': [genre.name for genre in movie.genres.all()],
                'average_rating': movie.average_rating,
                'video_link': movie.video_link,
            }
            return JsonResponse(data)
        return super().render_to_response(context, **response_kwargs)

class TrendingMoviesView(ListView):
    model = Movie
    template_name = 'trending.html'
    context_object_name = 'trending_movies'

    def get_queryset(self):
        return Movie.objects.order_by('-average_rating')[:10]

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            trending_movies = context['trending_movies']
            data = {
                'trending_movies': [
                    {
                        'id': movie.id,
                        'title': movie.title,
                        'description': movie.description,
                        'thumbnail': movie.thumbnail.url if movie.thumbnail else None,
                        'average_rating': movie.average_rating,
                    } for movie in trending_movies
                ]
            }
            return JsonResponse(data)
        return super().render_to_response(context, **response_kwargs)