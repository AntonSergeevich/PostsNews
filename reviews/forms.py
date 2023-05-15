from django import forms
from reviews.models import ContactForm


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['firstname', 'lastname', 'phone', 'email']



