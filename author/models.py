from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='Полное имя')
    is_alive = models.BooleanField(default=True)
    biography = models.TextField(max_length=1000, verbose_name='Биография', blank=True, null=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    @staticmethod
    def get_authors():
        return Author.objects.all()

    @staticmethod
    def get_alive_authors():
        return Author.objects.filter(is_alive=True)

    def get_books_list(self):
        return self.book_set.all()

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['name']
