from django.views.generic import FormView
from django.contrib import messages
from mysite.forms import ContactForm


class HomeView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = '/#contact'

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, "Thanks, We'll get back to you soon")
        return super().form_valid(form)
