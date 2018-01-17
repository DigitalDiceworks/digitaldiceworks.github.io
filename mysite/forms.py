from django import forms
from django.core.mail import send_mail

ADMIN_EMAILS = ['goldensly@hotmail.com']


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        error_messages={'required': 'Please enter your name.'}
    )
    email = forms.EmailField(
        error_messages={'required': 'Please enter your email address.'}
    )
    phone = forms.CharField(
        max_length=20,
        error_messages={'required': 'Please enter your phone number.'}
    )
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        error_messages={'required': 'Please enter a message.'}
    )

    def send_email(self):
        message = '\n\n'.join([
            f"Name: {self.cleaned_data['name']}",
            f"Email: {self.cleaned_data['email']}",
            f"Phone: {self.cleaned_data['phone']}",
            f"Message:\n{self.cleaned_data['message']}"
        ])

        send_mail(
            subject='Mail from site',
            message=message,
            from_email=None,
            recipient_list=ADMIN_EMAILS,
            fail_silently=False,
        )
