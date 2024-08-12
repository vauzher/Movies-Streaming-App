from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Rating, Like, Comment
from movies.models import Movie

@login_required
def rate_movie(request, movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, id=movie_id)
        value = request.POST.get('rating')
        Rating.objects.update_or_create(user=request.user, movie=movie, defaults={'value': value})
    return redirect('movie_detail', pk=movie_id)

@login_required
def like_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    Like.objects.get_or_create(user=request.user, movie=movie)
    return redirect('movie_detail', pk=movie_id)

@login_required
def comment_movie(request, movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, id=movie_id)
        content = request.POST.get('content')
        Comment.objects.create(user=request.user, movie=movie, content=content)
    return redirect('movie_detail', pk=movie_id)