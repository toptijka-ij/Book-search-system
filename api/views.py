from rest_framework.generics import RetrieveAPIView, GenericAPIView
from rest_framework.mixins import ListModelMixin

from api.serializers import BookSerializer, AuthorSerializer
from author.models import Author
from book.models import Book


class BookView(ListModelMixin, GenericAPIView):
    queryset = Book.get_all_by_date()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class SingleBookView(RetrieveAPIView):
    queryset = Book.get_all_by_date()
    serializer_class = BookSerializer


class AuthorView(ListModelMixin, GenericAPIView):
    queryset = Author.get_alive_authors()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class SingleAuthorView(RetrieveAPIView):
    queryset = Author.get_authors()
    serializer_class = AuthorSerializer
