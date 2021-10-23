from django.urls import path

from .views import detail, by_genre, AddBook, EditBook, DeleteBook, AddGenre, EditGenre, change_rating

app_name = 'book'
urlpatterns = [
    path('detail/<int:book_pk>/', detail, name='detail'),
    path('<int:genre_pk>/sort/<str:sort>/', by_genre, name='by_genre'),
    path('book_add/', AddBook.as_view(), name='book_add'),
    path('book_edit/<int:pk>/', EditBook.as_view(), name='book_edit'),
    path('book_delete/<int:pk>/', DeleteBook.as_view(), name='book_delete'),
    path('genre_add/', AddGenre.as_view(), name='genre_add'),
    path('genre_edit/<int:pk>/', EditGenre.as_view(), name='genre_edit'),
    path('<int:book_pk>/rating/', change_rating, name='change_rating')
]
