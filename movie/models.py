from django.db import models
import datetime as datetime_class
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField()
    duration = models.DurationField(null=False, blank=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.director}_{self.title}'


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.SmallIntegerField(default=3, validators=[MaxLengthValidator(5), MinLengthValidator(1)])

    def __str__(self):
        return f'{self.movie}_{self.text}'
