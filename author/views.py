from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView

from author.forms import AuthorForm
from author.models import Author
from main.mixins import AdminOrStaffRequiredMixin, AdminRequiredMixin


def author_page(request, author_pk):
    author = get_object_or_404(Author, pk=author_pk)
    books = author.get_books_list()
    context = {'author': author, 'books': books}
    return render(request, 'author/author_page.html', context)


class AddAuthor(AdminOrStaffRequiredMixin, CreateView):
    template_name = 'author/author_form.html'
    model = Author

    def get(self, request):
        form = AuthorForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Автор добавлен')
            return redirect('author:author_page', author_pk=Author.objects.latest('id').pk)
        else:
            form = AuthorForm()
            messages.add_message(request, messages.SUCCESS, 'Автор не добавлен')
        return render(request, self.template_name, {'form': form})


class EditAuthor(AdminOrStaffRequiredMixin, UpdateView):
    template_name = 'author/author_form.html'
    model = Author
    form_class = AuthorForm

    def get_success_url(self, **kwargs):
        author = get_object_or_404(Author, pk=self.object.pk)
        return reverse_lazy('author:author_page', kwargs={'author_pk': author.pk})


class DeleteAuthor(AdminRequiredMixin, DeleteView):
    template_name = 'author/author_delete.html'
    model = Author
    success_url = reverse_lazy('main:base')
