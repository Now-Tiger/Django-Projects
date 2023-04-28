from django.db import models
from django.utils import timezone

# Create your models here.


class Todo(models.Model):
    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField(
        max_length=100, unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICE, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self) -> str:
        return self.title
