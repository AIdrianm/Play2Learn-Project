
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutUsView(TemplateView):
    template_name = "pages/about_us.html"

class ContactUsPageView(TemplateView):
    template_name = "pages/contact_us.html"

class AdminPageView(TemplateView):
    template_name = "pages/admin.html"

class GamePageView(TemplateView):
    template_name = "pages/game.html"

class ReviewsPageView(TemplateView):
    template_name = "pages/reviews.html"

class LoginPageView(TemplateView):
    template_name = "pages/login.html"