from django import forms

from review.models import Review


class ReviewFormForBook(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['book']
