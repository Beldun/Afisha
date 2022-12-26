from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie.models import Director, Movie, Review
from movie.serializer import DirectorsSerializer, MoviesSerializer, ReviewsSerializer, MovieReviewSerializer
from movie.validation import MovieCreateSerializer, MovieUpdateSerializer, DirectorUpdateSerializer, \
    DirectorCreateSerializer, ReviewValidateSerializer
from rest_framework import status

# Create your views here.


@api_view(['GET', 'POST'])
def director_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorsSerializer(directors, many=True)

        return Response(data=serializer.data)

    elif request.method == 'POST':
        serializer = DirectorCreateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,

                            data={'errors': serializer.errors})

        name = serializer.validated_data.get('name')

        directors = Director.objects.create(name=name)
        directors.save()

        return Response(data={'message': "Data received!",
                              "director": DirectorsSerializer(directors).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_view(request, **kwargs):
    try:
        directors = Director.objects.get(id=kwargs['id'])
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Page not found!'})

    if request.method == 'GET':
        serializer = DirectorsSerializer(directors, many=False)

        return Response(data=serializer.data)

    elif request.method == 'DELETE':
        directors.delete()

        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={'message': 'Data deleted!'})

    else:
        serializer = DirectorUpdateSerializer(data=request.data,
                                              context={'id': directors.id})

        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,

                            data={'errors': serializer.errors})

        directors.name = serializer.validated_data.get('name')
        directors.save()

        return Response(data={'message': "Data received!",
                              "director": DirectorsSerializer(directors).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def movie_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MoviesSerializer(movies, many=True)

        return Response(data=serializer.data)

    elif request.method == 'POST':
        serializer = MovieCreateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,

                            data={'errors': serializer.errors})

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director = serializer.validated_data.get('director')

        movies = Movie.objects.create(title=title, description=description, duration=duration, director_id=director)
        movies.save()

        return Response(data={'message': "Data received!",
                              "movie": MoviesSerializer(movies).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request, **kwargs):
    try:
        movies = Movie.objects.get(id=kwargs['id'])
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Page not found!'})

    if request.method == 'GET':
        serializer = MoviesSerializer(movies, many=False)

        return Response(data=serializer.data)

    elif request.method == 'DELETE':
        movies.delete()

        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={'message': 'Data deleted!'})

    else:
        serializer = MovieUpdateSerializer(data=request.data,
                                           context={'id': movies.id})
        serializer.is_valid(raise_exception=True)

        movies.title = serializer.validated_data.get('title')
        movies.description = serializer.validated_data.get('description')
        movies.duration = serializer.validated_data.get('duration')
        movies.director_id = serializer.validated_data.get('director')
        movies.save()

        return Response(data={'message': 'Data received!',
                              "movie": MoviesSerializer(movies).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def review_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()

        serializer = ReviewsSerializer(reviews, many=True)

        return Response(data=serializer.data)

    elif request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,

                            data={'errors': serializer.errors})

        text = serializer.validated_data.get('text')
        movie = serializer.validated_data.get('movie')
        stars = serializer.validated_data.get('stars')

        reviews = Review.objects.create(text=text, movie_id=movie, stars=stars)
        reviews.save()

        return Response(data={'message': "Data received!",
                              "review": ReviewsSerializer(reviews).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, **kwargs):
    try:
        reviews = Review.objects.get(id=kwargs['id'])
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Page not found!'})

    if request.method == 'GET':
        serializer = ReviewsSerializer(reviews, many=False)

        return Response(data=serializer.data)

    elif request.method == 'DELETE':
        reviews.delete()

        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={'message': 'Data deleted!'})

    else:
        serializer = ReviewValidateSerializer(data=request.data,
                                              context={'id': reviews.id})

        serializer.is_valid(raise_exception=True)
        reviews.text = serializer.validated_data.get('text')
        reviews.movie_id = serializer.validated_data.get('movie')
        reviews.stars = serializer.validated_data.get('stars')
        reviews.save()

        return Response(data={'message': "Data received!",
                              "review": ReviewsSerializer(reviews).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movie_review_view(request, **kwargs):
    if request.method == 'GET':
        movie = Movie.objects.all()

        serializer = MovieReviewSerializer(movie, many=True)

        return Response(data=serializer.data)
