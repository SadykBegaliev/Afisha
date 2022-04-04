from django.db import models
from statistics import mean


class Director(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @property
    def movies_count(self):
        return self.movies.count()




class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True,
                                 related_name='movies')

    def __str__(self):
        return self.title


    @property
    def filtered_reviews(self):
        return self.reviews.filter(stars__gte=4)


    @property
    def reviews_count(self):
        return self.filtered_reviews.count()

    @property
    def rating(self):
        reviews = self.filtered_reviews
        count = reviews.count()
        if count == 0:
            return 0
        sum_ = 0
        for i in reviews:
            sum_ += i.stars
        return sum_ / count

CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

class Review(models.Model):
    text = models.TextField()
    movies = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True,
                              related_name='reviews')
    stars = models.IntegerField(default=1, choices=CHOICES)

    def __str__(self):
        return self.text
