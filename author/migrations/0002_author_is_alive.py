# Generated by Django 3.2.4 on 2021-09-15 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='is_alive',
            field=models.BooleanField(default=True),
        ),
    ]
