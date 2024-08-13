from django.urls import path
from . import views

urlpatterns = [
    path('rate/<int:movie_id>/', views.rate_movie, name='rate_movie'),
    path('like/<int:movie_id>/', views.like_movie, name='like_movie'),
    path('comment/<int:movie_id>/', views.comment_movie, name='comment_movie'),
    path('add-to-list/<int:movie_id>/', views.add_to_list, name='add_to_list'),
    path('remove-from-list/<int:movie_id>/', views.remove_from_list, name='remove_from_list'),
    path('my-list/', views.view_user_list, name='view_user_list'),
    
]