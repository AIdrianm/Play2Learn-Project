from django.db import models
from django.urls import reverse
# Create your models here.
class Review(models.Model):
    review = models.TextField(max_length=127)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review

    def get_absolute_url(self):
        return reverse('reviews:review_detail', args=[str(self.id)])