from django import forms
from .models import Author, Quote

class AuthorForm(forms.ModelForm):
    fullname = forms.CharField(max_length=50, required=True)
    born_date = forms.CharField(max_length=50)
    born_location = forms.CharField(max_length=50)
    description = forms.Textarea

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

class QuoteForm(forms.ModelForm):
    quote = forms.Textarea
    author = forms.CharField(max_length=50, required=True)

    class Meta:
        model = Quote
        fields = ['quote', 'author']
        exclude = ['tags']