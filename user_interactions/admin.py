from django.contrib import admin
from .models import Comment, Like, Rating, UserList

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'content', 'created_at')
    search_fields = ('user__username', 'movie__title')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'created_at')
    search_fields = ('user__username', 'movie__title')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'value', 'created_at')
    search_fields = ('user__username', 'movie__title')


@admin.register(UserList)
class List(admin.ModelAdmin):
    list_display = ('user',)