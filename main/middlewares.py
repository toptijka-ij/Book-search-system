from book.forms import RatingForm
from book.models import Genre
from .forms import SearchForm


def genre_context_processor(request):
    context = {'genres': Genre.get_all()}
    return context


def search_form_context_processor(request):
    context = {'search_form': SearchForm()}
    return context


def rating_form_context_processor(request):
    context = {'rating_form': RatingForm()}
    return context
