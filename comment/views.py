from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from django.views.generic.base import View

from book.models import Book
from .forms import CommentForm
from .models import Comment


class AddComment(View):

    def post(self, request, book_pk):
        form = CommentForm(request.POST)
        book = Book.objects.get(id=book_pk)
        user = request.user
        if form.is_valid():
            print(request.POST)
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.book = book
            form.user = user
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Комментарий добавлен')
        else:
            messages.add_message(request, messages.WARNING, 'Комментарий не добавлен')
        return redirect(book.get_absolute_url())


class EditComment(UpdateView):
    template_name = 'comment/comment_form.html'
    model = Comment
    form_class = CommentForm

    def get_success_url(self, **kwargs):
        book = get_object_or_404(Book, pk=self.object.book.pk)
        return reverse_lazy('book:detail', kwargs={'book_pk': book.pk})


class DeleteComment(DeleteView):
    template_name = 'comment/comment_delete.html'
    model = Comment

    def get_success_url(self, **kwargs):
        book = get_object_or_404(Book, pk=self.object.book.pk)
        return reverse_lazy('book:detail', kwargs={'book_pk': book.pk})
