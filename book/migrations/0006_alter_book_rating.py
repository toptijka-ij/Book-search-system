# Generated by Django 3.2.4 on 2021-08-30 14:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('book', '0005_alter_book_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(5)],
                                    verbose_name='Рейтинг'),
        ),
    ]
