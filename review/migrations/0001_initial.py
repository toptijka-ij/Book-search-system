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
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=5000, verbose_name='Текст')),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='book.book',
                                              verbose_name='Книга')),
            ],
            options={
                'verbose_name': 'Рецензия',
                'verbose_name_plural': 'Рецензии',
            },
        ),
    ]
