from django.urls import path
from . import views

urlpatterns = [
    path('rate/<int:movie_id>/', views.rate_movie, name='rate_movie'),
    path('like/<int:movie_id>/', views.like_movie, name='like_movie'),
    path('comment/<int:movie_id>/', views.comment_movie, name='comment_movie'),
]