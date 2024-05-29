import html
from django.urls import reverse_lazy
from .forms import ContactUsForm
from django.views.generic import FormView, TemplateView
from common.utils.email import send_email


class AdminPageView(TemplateView):
    template_name = "pages/admin.html"

class AboutUsView(TemplateView):
    template_name = "pages/about_us.html"

class ContactUsThanksPageView(TemplateView):
    template_name = "pages/thanks.html"

class ContactUsPageView(FormView):
    template_name = 'pages/contact_us.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('pages:thanks')

    def form_valid(self, form):
        data = form.cleaned_data
        to = 'officialadrianmontiel@gmail.com'
        subject = 'Contact Us Form Submission'
        content = f'''<p>Hey Administrator!</p>
            <p>Contact us form received:</p>
            <ol>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>'
        
        content += '</ol>'

        send_email(to, subject, content)
        return super().form_valid(form)

class GamePageView(TemplateView):
    template_name = "pages/game.html"

class HomePageView(TemplateView):
    template_name = "pages/home.html"


class LoginPageView(TemplateView):
    template_name = "pages/login.html"



