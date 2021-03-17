from django.db import models
from datetime import datetime


class Posts(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title
