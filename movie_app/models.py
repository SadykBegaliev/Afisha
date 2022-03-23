from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    director_foreign_key = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField()
    movie_foreign_key = models.PositiveIntegerField()

    def __str__(self):
        return self.text

