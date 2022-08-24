from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    rating = models.FloatField()
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.PositiveIntegerField(default=0)
    movie_title = models.CharField(max_length=255)
    movie_img = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.movie_title

