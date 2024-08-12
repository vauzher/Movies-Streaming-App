from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Rating, Like, Comment
from movies.models import Movie
from django.shortcuts import redirect, get_object_or_404  # Import get_object_or_404
from django.http import JsonResponse

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
    
    # Check if the user has already liked the movie
    like, created = Like.objects.get_or_create(user=request.user, movie=movie)
    
    if not created:
        # If the like already exists, remove it (unlike functionality)
        like.delete()
        liked = False
    else:
        # If the like was created, it means the user just liked the movie
        liked = True

    # Get the updated like count
    like_count = Like.objects.filter(movie=movie).count()

    # Return the response as JSON
    return JsonResponse({'new_like_count': like_count, 'liked': liked})

@login_required
def comment_movie(request, movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, id=movie_id)
        content = request.POST.get('content')
        Comment.objects.create(user=request.user, movie=movie, content=content)
    return redirect('movie_detail', pk=movie_id)