from django.db import models
from django.contrib.auth.models import AbstractUser


class UserRole(models.TextChoices):
    USER = 'user', 'Пользователь'
    MODERATOR = 'moderator', 'Модератор'
    ADMIN = 'admin', 'Администратор'


class User(AbstractUser):
    email = models.EmailField('Email адрес', unique=True)

    bio = models.TextField(
        blank=True,
        verbose_name='Биография'
    )
    role = models.CharField(
        max_length=16,
        choices=UserRole.choices,
        blank=True,
        default='user',
        verbose_name=UserRole.USER
    )

    @property
    def is_user(self):
        return self.role == UserRole.USER

    @property
    def is_moderator(self):
        return self.role == UserRole.MODERATOR

    @property
    def is_admin(self):
        return self.role == UserRole.ADMIN

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username
