from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Rating, Like, Comment, UserList
from movies.models import Movie
from django.contrib import messages

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
    like, created = Like.objects.get_or_create(user=request.user, movie = movie)
    if not created:
        like.delete()
    return redirect('movie_detail', pk=movie_id)


@login_required
def comment_movie(request, movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, id=movie_id)
        content = request.POST.get('content')
        Comment.objects.create(user=request.user, movie=movie, content=content)
    return redirect('movie_detail', pk=movie_id)

@login_required
def add_to_list(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    user_list, created = UserList.objects.get_or_create(user=request.user)
    if movie not in user_list.movies.all():
        user_list.movies.add(movie)
        messages.success(request, f'{movie.title} was added to your list!')
    else:
        messages.info(request, f'{movie.title} is already in your list.')
    return redirect('movie_detail', pk = movie_id)

@login_required
def remove_from_list(request, movie_id):
    movie = get_object_or_404(Movie, id = movie_id)
    user_list = get_object_or_404(UserList, user = request.user)
    if movie in user_list.movies.all():
        user_list.movies.remove(movie)
        messages.success(request, f'{movie.title} was removed from your list!')
    else:
        messages.error(request, f'{movie.title} is not in your list.')
    return redirect('movie_detail', pk = movie_id)
@login_required
def view_user_list(request):
    user_list, created = UserList.objects.get_or_create(user=request.user)
    return render(request, 'view_user_list.html', {'user_list': user_list})