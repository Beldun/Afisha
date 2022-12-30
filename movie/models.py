from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return f'{self.name}'


class Movie(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField()
    duration = models.IntegerField(default=0)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return f'{self.title} - {self.director}'


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(default=3, choices=(
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ))
    created_date = models.DateField(auto_now_add=True, null=True)
    modified_date = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.text}'
