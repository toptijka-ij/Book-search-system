from django.db import models

from book.models import Book


class Review(models.Model):
    text = models.TextField(max_length=5000, verbose_name='Текст')
    # comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    book = models.OneToOneField(Book, on_delete=models.CASCADE, verbose_name='Книга')

    def __str__(self):
        return str(self.book)

    class Meta:
        verbose_name = 'Рецензия'
        verbose_name_plural = 'Рецензии'
