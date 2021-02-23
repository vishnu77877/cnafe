from django import forms
import datetime


class ContactForm(forms.Form):
    date = forms.DateField(label='Starting Date', initial='YYYY-MM-DD')
