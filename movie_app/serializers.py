from rest_framework import serializers
from movie_app.models import Director, Movie, Review


class ReviewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars'.split()


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name movies_count'.split()


class MoviesSerializers(serializers.ModelSerializer):
    director = DirectorSerializers()
    reviews = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = 'title description duration director reviews reviews_count rating'.split()

    def get_reviews(self, movies):
        return ReviewsSerializers(movies.filtered_reviews, many=True).data
