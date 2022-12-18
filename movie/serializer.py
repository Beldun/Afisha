from rest_framework import serializers
from movie.models import Director, Movie, Review


class DirectorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'name')


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director')


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'movie', 'stars')


class MovieReviewSerializer(serializers.ModelSerializer):
    director = serializers.SerializerMethodField()
    reviews = ReviewsSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director', 'reviews')

    def get_director(self, movie):
        return movie.director.name if movie.director else None



