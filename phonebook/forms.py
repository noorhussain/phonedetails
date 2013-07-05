from django.forms import ModelForm
from phonebook.models import Contact, PhoneNo

class ContactForm(ModelForm):
    class Meta:
        model = Contact

class PhoneNoForm(ModelForm):
    class Meta:
        model = PhoneNo
