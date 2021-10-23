from django.urls import path

from api.views import BookView, SingleBookView, AuthorView, SingleAuthorView

urlpatterns = [
    path('books/', BookView.as_view()),
    path('books/<int:pk>', SingleBookView.as_view()),
    path('authors/', AuthorView.as_view()),
    path('authors/<int:pk>', SingleAuthorView.as_view()),
]
