from django.urls import path

from .views import AboutUsView, AdminPageView, ContactUsPageView, GamePageView, HomePageView, LoginPageView, ReviewsPageView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('about/', AboutUsView.as_view(), name='about'),
    path('admin/', AdminPageView.as_view(), name='admin'),
    path('contact-us/', ContactUsPageView.as_view(), name='contact-us'),
    path('games/', GamePageView.as_view(), name='games'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('reviews/', ReviewsPageView.as_view(), name='reviews')
]