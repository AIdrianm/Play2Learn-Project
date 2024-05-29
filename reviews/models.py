from django.db import models
from django.conf import settings


class Review(models.Model):
    review = models.TextField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review + ' | ' + self.user.username