from django.views.generic import FormView
from mysite.forms import ContactForm


class HomeView(FormView):
    template_name = 'home.html'
    form_class = ContactForm
    success_url = '/#contact'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
