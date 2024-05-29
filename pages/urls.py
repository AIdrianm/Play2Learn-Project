from django.urls import path

from .views import AboutUsView, AdminPageView, ContactUsPageView, ContactUsThanksPageView, GamePageView, HomePageView, LoginPageView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('about/', AboutUsView.as_view(), name='about'),
    path('admin/', AdminPageView.as_view(), name='admin'),
    path('contact-us/', ContactUsPageView.as_view(), name='contact-us'),
    path('thanks/', ContactUsThanksPageView.as_view(), name='thanks'),
    path('games/', GamePageView.as_view(), name='games'),
    path('login/', LoginPageView.as_view(), name='login'),
   
]