from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie.models import Director, Movie, Review
from movie.serializer import DirectorsSerializer, MoviesSerializer, ReviewsSerializer, MovieReviewSerializer
from rest_framework import status

# Create your views here.


@api_view(['GET'])
def director_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()

        serializer = DirectorsSerializer(directors, many=True)

        return Response(data=serializer.data)


@api_view(['GET'])
def director_detail_view(request, **kwargs):
    if request.method == 'GET':
        try:
            directors = Director.objects.get(id=kwargs['id'])
        except Director.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'message': 'Page not found!'})

        serializer = DirectorsSerializer(directors, many=False)

        return Response(data=serializer.data)


@api_view(['GET'])
def movie_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()

        serializer = MoviesSerializer(movies, many=True)

        return Response(data=serializer.data)


@api_view(['GET'])
def movie_detail_view(request, **kwargs):
    if request.method == 'GET':
        try:
            movies = Movie.objects.get(id=kwargs['id'])
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'message': 'Page not found!'})

        serializer = MoviesSerializer(movies, many=False)

        return Response(data=serializer.data)


@api_view(['GET'])
def review_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()

        serializer = ReviewsSerializer(reviews, many=True)

        return Response(data=serializer.data)


@api_view(['GET'])
def review_detail_view(request, **kwargs):
    if request.method == 'GET':
        try:
            reviews = Review.objects.get(id=kwargs['id'])
        except Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'message': 'Page not found!'})

        serializer = ReviewsSerializer(reviews, many=False)

        return Response(data=serializer.data)


@api_view(['GET'])
def movie_review_view(request, **kwargs):
    if request.method == 'GET':
        movie = Movie.objects.all()

        serializer = MovieReviewSerializer(movie, many=True)

        return Response(data=serializer.data)

