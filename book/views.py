from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from book.forms import BookForm, GenreForm, RatingForm
from book.models import Book, Genre
from comment.forms import CommentForm
from main.mixins import AdminOrStaffRequiredMixin, AdminRequiredMixin


def change_rating(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            mark = request.POST.get("rating")
            book.add_mark(int(mark))
            messages.add_message(request, messages.SUCCESS, 'Ваша оценка учтена')
        else:
            form = RatingForm()
            messages.add_message(request, messages.WARNING, 'Ваша оценка не учтена')
    return redirect(book.get_absolute_url())


def detail(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    comments = book.get_comments()
    c_form = CommentForm()
    context = {'book': book, 'comments': comments, 'c_form': c_form}
    return render(request, 'book/detail.html', context)


def by_genre(request, genre_pk, sort):
    genre = get_object_or_404(Genre, pk=genre_pk)
    books = []
    if sort == 'date':
        books = Book.get_all_by_date().filter(genre=genre_pk)
    elif sort == 'rating':
        books = Book.get_all_by_rating().filter(genre=genre_pk)
    # books = Book.objects.filter(genre=genre_pk)
    paginator = Paginator(books, 10)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, 'book/by_genre.html', {'genre': genre, 'books': books, 'page': page})


class AddBook(AdminOrStaffRequiredMixin, CreateView):
    template_name = 'book/book_form.html'
    model = Book

    def get(self, request):
        form = BookForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Книга добавлена')
            return redirect('main:base')
        else:
            form = BookForm()
            messages.add_message(request, messages.SUCCESS, 'Книга не добавлена')
        return render(request, self.template_name, {'form': form})


class EditBook(AdminOrStaffRequiredMixin, UpdateView):
    template_name = 'book/book_form.html'
    model = Book
    form_class = BookForm

    def get_success_url(self, **kwargs):
        book = get_object_or_404(Book, pk=self.object.pk)
        return reverse_lazy(book.get_absolute_url())


class DeleteBook(AdminOrStaffRequiredMixin, DeleteView):
    template_name = 'book/book_delete.html'
    model = Book

    def get_success_url(self, **kwargs):
        book = get_object_or_404(Book, pk=self.object.pk)
        return reverse_lazy(book.get_absolute_url())


class AddGenre(AdminRequiredMixin, ListView):
    template_name = 'book/genre_form.html'
    model = Genre

    def get(self, request):
        form = GenreForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Жанр добавлен')
            return redirect('main:base')
        else:
            form = GenreForm()
            messages.add_message(request, messages.SUCCESS, 'Жанр не добавлен')
        return render(request, self.template_name, {'form': form})


class EditGenre(AdminRequiredMixin, UpdateView):
    template_name = 'book/genre_form.html'
    model = Genre
    form_class = GenreForm
    success_url = reverse_lazy('main:base')
