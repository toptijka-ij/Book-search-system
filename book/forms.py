from django import forms

from book.models import Book, Genre, MAX_MARK


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['added_at']


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        exclude = '__all__'


class RatingForm(forms.Form):
    CHOICES = [(x, x) for x in range(1, MAX_MARK + 1)]
    rating = forms.IntegerField(label='',
                                widget=forms.RadioSelect(choices=CHOICES, attrs={'class': 'form-check-inline'}),
                                min_value=1, max_value=MAX_MARK)

    # def __init__(self, *args, **kwargs):
    #     super(Book, Book.objects.first()).__init__(*args, **kwargs)
    #     self.fields['rating'].widget.attrs['cols'] = 10
