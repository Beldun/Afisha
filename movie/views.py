from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie.models import Director, Movie, Review
from movie.serializer import DirectorsSerializer, MoviesSerializer, ReviewsSerializer, MovieReviewSerializer
from movie.validation import MovieCreateSerializer, MovieUpdateSerializer, DirectorUpdateSerializer, \
    DirectorCreateSerializer, ReviewValidateSerializer
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class DirectorView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorsSerializer

    def post(self, request, *args, **kwargs):
        serializer = DirectorCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get('name')

        directors = Director.objects.create(name=name)
        directors.save()

        return Response(data={'message': "Data received!",
                              "director": DirectorsSerializer(directors).data},
                        status=status.HTTP_201_CREATED)


class DirectorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorsSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        directors = Director.objects.get(id=kwargs['id'])

        serializer = DirectorUpdateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        directors.name = serializer.validated_data.get('name')
        directors.save()

        return Response(data={'message': "Data received!",
                              "director": DirectorsSerializer(directors).data},
                        status=status.HTTP_201_CREATED)


class MovieView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer

    def post(self, request, *args, **kwargs):
        serializer = MovieCreateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director = serializer.validated_data.get('director')

        movies = Movie.objects.create(title=title, description=description, duration=duration, director_id=director)
        movies.save()

        return Response(data={'message': "Data received!",
                              "movie": MoviesSerializer(movies).data},
                        status=status.HTTP_201_CREATED)


class MovieDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        movies = Movie.objects.get(id=kwargs['id'])

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


class ReviewView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer

    def post(self, request, *args, **kwargs):
        serializer = ReviewValidateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        text = serializer.validated_data.get('text')
        movie = serializer.validated_data.get('movie')
        stars = serializer.validated_data.get('stars')

        reviews = Review.objects.create(text=text, movie_id=movie, stars=stars)
        reviews.save()

        return Response(data={'message': "Data received!",
                              "review": ReviewsSerializer(reviews).data},
                        status=status.HTTP_201_CREATED)


class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        reviews = Review.objects.get(id=kwargs['id'])

        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        reviews.text = serializer.validated_data.get('text')
        reviews.movie_id = serializer.validated_data.get('movie')
        reviews.stars = serializer.validated_data.get('stars')
        reviews.save()

        return Response(data={'message': "Data received!",
                              "review": ReviewsSerializer(reviews).data},
                        status=status.HTTP_201_CREATED)


class ReviewMovieView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieReviewSerializer
