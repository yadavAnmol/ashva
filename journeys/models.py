from django.db import models
from django.utils import timezone

class Photo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="photos/")
    created_at = models.DateTimeField(default=timezone.now)  # ✅ add default

    def __str__(self):
        return self.title
