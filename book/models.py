from datetime import date, datetime
from os.path import splitext

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

from author.models import Author

MAX_MARK = 5


class Genre(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name']

    @staticmethod
    def get_all():
        return Genre.objects.all()


def current_year():
    return date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


def get_timestamp_path(instance, filename):
    return '%s%s' % (datetime.now().timestamp(), splitext(filename)[1])


class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=2000, verbose_name='Описание')
    published_year = models.PositiveIntegerField(validators=[MinValueValidator(1900), max_value_current_year],
                                                 verbose_name='Год публикации', default=current_year)
    cover = models.ImageField(upload_to=get_timestamp_path, verbose_name='Обложка')
    added_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Дата добавления на сайт')
    authors = models.ManyToManyField(Author, verbose_name='Авторы')
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, verbose_name='Жанр')
    rating = models.FloatField(validators=[MaxValueValidator(MAX_MARK)], verbose_name='Рейтинг', default=0)

    def __str__(self):
        return self.name + ' (' + ', '.join([author.name for author in self.authors.all()]) + ')'

    def __repr__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book:detail', kwargs={'book_pk': self.pk})

    def get_comments(self):
        return self.comment_set.filter(parent__isnull=True)

    def add_mark(self, new_mark):
        if self.rating:
            self.rating = (self.rating + new_mark) / 2
            self.save(update_fields=['rating'])
        else:
            self.rating = new_mark
            self.save(update_fields=['rating'])

    # def delete(self, *args, **kwargs):
    #     self.cover.delete()
    #     super().delete(*args, **kwargs)

    def get_authors_list(self):
        return self.authors.all()

    @staticmethod
    def get_all_by_date():
        return Book.objects.all()

    @staticmethod
    def get_all_by_rating():
        return Book.objects.order_by('-rating')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-added_at']
