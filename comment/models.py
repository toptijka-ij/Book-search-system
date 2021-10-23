from django.db import models

from book.models import Book
from main.models import CustomUser


class Comment(models.Model):
    text = models.TextField(max_length=500, verbose_name='Текст комментария')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга, которую комментируют')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Комментатор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликован')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Комментарий к комментарию',
                               related_name='+', blank=True, null=True)

    def __str__(self):
        return self.user.username + ', ' + self.book.name + ', ' + self.text

    @property
    def children(self):
        return Comment.objects.filter(parent=self).order_by('-created_at').all()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['created_at']
