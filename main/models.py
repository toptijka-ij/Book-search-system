from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    send_messages = models.BooleanField(default=True, verbose_name='Слать оповещения о новых комментариях?')

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        pass
