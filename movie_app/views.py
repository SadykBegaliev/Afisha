from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import DirectorSerializers, MoviesSerializers, ReviewsSerializers
from movie_app.models import Director, Movie, Review
from rest_framework import status

### РЕЖИССЕР #################################################
@api_view(['GET'])
def director_list(request):
    director = Director.objects.all()
    serializer = DirectorSerializers(director, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def director_item(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error':'Director not found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = DirectorSerializers(director)
    return Response(data=serializer.data)

### ФИЛЬМ ######################################################
@api_view(['GET'])
def movies_list(request):
    movie = Movie.objects.all()
    serializer = MoviesSerializers(movie, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def movie_item(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error':'Movie not found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = MoviesSerializers(movie)
    return Response(data=serializer.data)

### ОТЗЫВ #########################################################
@api_view(['GET'])
def reviews_list(request):
    review = Review.objects.all()
    serializer = ReviewsSerializers(review, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def review_item(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error':'Review not found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewsSerializers(review)
    return Response(data=serializer.data)