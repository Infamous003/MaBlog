from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    tags = [
        ('tech', 'Tech'),
        ('cs', 'Computer Science'),
        ('ai', 'AI'),
        ('bio', 'Biology'),
        ('music', 'Music'),
        ('movies', 'Movies'),
        ('psychology', 'Psychology'),
        ('history', 'History'),
        ('books', 'Books & Literature'),
        ('fiction', 'Fiction'),
        ('gaming', 'Gaming'),
        ('other', 'Other'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=130)
    subtitle = models.CharField(max_length=70, blank=True)
    content = models.TextField()
    tags = models.CharField(max_length=50, choices=tags, default='other')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title