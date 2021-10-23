from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from author.models import Author
from book.models import Book
from .forms import ChangeUserInfoForm, SearchForm, RegisterUserForm
from .models import CustomUser


def handler_not_found(request, exception):
    return render(request, 'errors/404.html')


def handler_perm_denied(request, exception):
    return render(request, 'errors/403.html')


def handler_server_error(request, *args, **kwargs):
    return render(request, 'errors/500.html')


def handler_bad_gateway(request, exception):
    return render(request, 'errors/400.html')


def search(request):
    keyword = None
    results = {'b_results': [], 'a_results': []}
    if 'keyword' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            results['b_results'] = Book.objects.filter(name__icontains=keyword)
            results['a_results'] = Author.objects.filter(name__icontains=keyword)
    return render(request, 'main/search.html', {'results': results, 'keyword': keyword})


def base(request):
    return redirect('main:index', sort='date')


def index(request, sort):
    books = []
    if sort == 'date':
        books = Book.get_all_by_date()
    elif sort == 'rating':
        books = Book.get_all_by_rating()
    paginator = Paginator(books, 10)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, 'main/index.html', {'page': page, 'books': books})


class BBLoginView(LoginView):
    template_name = 'main/login.html'


@login_required
def profile(request):
    return render(request, 'main/profile.html')


class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'main/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('main:profile')
    success_message = 'Данные пользователя изменены'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class BBPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'main/password_change.html'
    success_url = reverse_lazy('main:profile')
    success_message = 'Пароль пользователя изменен'


class RegisterUserView(CreateView):
    model = CustomUser
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'main/delete_user.html'
    success_url = reverse_lazy('main:base')

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'Пользователь удален')
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)
