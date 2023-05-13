from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import User
from core.models import AddNameModel
from .validators import validate_year


class Category(AddNameModel):
    slug = models.SlugField(unique=True, max_length=50)

    class Meta:
        verbose_name = 'Категория'

    def __str__(self) -> str:
        return f'{self.name} {self.slug}'


class Genre(AddNameModel):
    slug = models.SlugField(unique=True, max_length=50)

    class Meta:
        verbose_name = 'Жанр'

    def __str__(self) -> str:
        return f'{self.name} {self.slug}'


class Title(AddNameModel):
    year = models.PositiveSmallIntegerField(validators=[validate_year])
    description = models.TextField(
        verbose_name='Описание произведения',
        blank=True,
        null=True,
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='жанр',
        through='GenreTitle'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='категория',
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Произведение'
        ordering = ['-year']


class Review(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор отзыва',
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='ID произведения',
    )
    text = models.TextField(
        verbose_name='Текст отзыва',
    )
    score = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
        verbose_name='Оценка',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата публикации',
    )

    def __str__(self) -> str:
        return self.text

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title_id'],
                name='unique_reviews'
            )
        ]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор коммента',
    )
    review_id = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='ID отзыва',
    )
    text = models.TextField(
        verbose_name='Текст комментария',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата публикации комментария',
    )

    def __str__(self) -> str:
        return self.text

    class Meta():
        ordering = ['-pub_date']


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.genre} {self.title}'
