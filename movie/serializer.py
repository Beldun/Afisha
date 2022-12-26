from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from movie.models import Director, Movie, Review


class DirectorsSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ('id', 'name', 'movies_count')

    def get_movies_count(self, directors):
        return directors.movies.all().count()


class MoviesSerializer(serializers.ModelSerializer):
    director = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director')

    def get_director(self, movie):
        return movie.director.name if movie.director else None


class ReviewsSerializer(serializers.ModelSerializer):
    movie = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ('id', 'text', 'movie', 'stars')

    def get_movie(self, review):
        return review.movie.title if review.movie.title else None


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = 'movie'.split()


class MovieReviewSerializer(serializers.ModelSerializer):
    director = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director', 'reviews', 'average_rating',)

    def get_director(self, movie):
        return movie.director.name if movie.director else None

    def get_average_rating(self, movie):
        lst = [review.stars for review in movie.reviews.all()]
        return sum(lst) / len(lst) if lst else None
