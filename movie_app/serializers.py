from rest_framework import serializers
from movie_app.models import Director, Movie, Review

class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name'.split()
        # fields = '__all__'

class MoviesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = 'name'.split()
        fields = '__all__'

class ReviewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        # fields = 'name'.split()
        fields = '__all__'