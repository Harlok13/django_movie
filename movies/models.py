from datetime import date
from django.db import models


class Category(models.Model):
    """Категории"""
    name = models.CharField('Категория', max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Actor(models.Model):
    """Актёры и режиссёры"""
    name = models.CharField('Имя', max_length=100)
    age = models.PositiveSmallIntegerField('Возраст', default=0)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актёры и режиссёры'
        verbose_name_plural = 'Актёры и режиссёры'


class Genre(models.Model):
    """Жанры"""
    name = models.CharField('Имя', max_length=100)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(models.Model):
    """Фильм"""
    title = models.CharField('Название', max_length=100)
    tagline = models.CharField('Слоган', max_length=100, default='')
    description = models.TextField('Описание')
    poster = models.ImageField('Постер', upload_to='movies/')
    year = models.PositiveSmallIntegerField('Дата выхода', default=2022)
    country = models.CharField('Страна', max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name='Режиссёр', related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='Актёр', related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbose_name='Жанр')
    world_premier = models.DateField('Премьера в мире', default=date.today)
    budget = models.PositiveIntegerField('Бюджет', default=0, help_text='указывать сумму в долларах')
    fees_in_usa = models.PositiveIntegerField('Сборы в США', default=0, help_text='указывать сумму в долларах')
    fees_in_world = models.PositiveIntegerField('Сборы в мире', default=0, help_text='указывать сумму в долларах')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField('Черновик', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class MovieShots(models.Model):
    """Кадры из фильма"""
    title = models.CharField('Название', max_length=100)
    descriptions = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильмов'


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField('Значение', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField('IP адрес', max_length=15)
    star = models.ForeignKey(RatingStar, verbose_name='Звезда', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CharField)

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Сообщение', max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(Movie, verbose_name='фильм', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'





