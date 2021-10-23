from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView

from book.models import Book
from main.mixins import AdminOrStaffRequiredMixin, AdminRequiredMixin
from .decorators import allowed_users
from .forms import ReviewFormForBook
from .models import Review


@allowed_users(allowed_roles=['admin', 'staff'])
def add_review(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    form = ReviewFormForBook()
    if request.method == 'POST':
        form = ReviewFormForBook(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.book = book
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Рецензия добавлена')
            return redirect('book:detail', book_pk=book.pk, genre_pk=book.genre.pk)
        else:
            form = ReviewFormForBook()
            messages.add_message(request, messages.WARNING, 'Рецензия не добавлена')
    return render(request, 'review/review_form.html', {'form': form})


class EditReview(AdminOrStaffRequiredMixin, UpdateView):
    template_name = 'review/review_form.html'
    model = Review
    form_class = ReviewFormForBook

    def get_success_url(self, **kwargs):
        book = get_object_or_404(Book, pk=self.object.book.pk)
        return reverse_lazy('book:detail', kwargs={'book_pk': book.pk})


class DeleteReview(AdminRequiredMixin, DeleteView):
    template_name = 'review/review_delete.html'
    model = Review

    def get_success_url(self, **kwargs):
        book = get_object_or_404(Book, pk=self.object.book.pk)
        return reverse_lazy('book:detail', kwargs={'book_pk': book.pk})
