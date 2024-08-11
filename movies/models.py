from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    genres = models.ManyToManyField(Genre)
    video_link = models.URLField()
    thumbnail = models.ImageField(upload_to='movie_thumbnails/')
    average_rating = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    views = models.IntegerField(default=0)  # Track the number of views
    likes = models.IntegerField(default=0)  # Track the number of likes
    created_at = models.DateTimeField(auto_now_add=True)  # Track when the movie was added

    def __str__(self):
        return self.title
