# Generated by Django 3.2.4 on 2021-08-29 15:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500, verbose_name='Текст комментария')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Опубликован')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book',
                                           verbose_name='Книга, которую комментируют')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['created_at'],
            },
        ),
    ]
