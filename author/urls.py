from django.urls import path

from .views import author_page, AddAuthor, EditAuthor, DeleteAuthor

app_name = 'author'
urlpatterns = [
    path('<int:author_pk>/', author_page, name='author_page'),
    path('author_add/', AddAuthor.as_view(), name='author_add'),
    path('author_edit/<int:pk>', EditAuthor.as_view(), name='author_edit'),
    path('author_delete/<int:pk>', DeleteAuthor.as_view(), name='author_delete'),
]
