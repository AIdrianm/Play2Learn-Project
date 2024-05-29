from django.views.generic import ListView
from .models import Review

class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'