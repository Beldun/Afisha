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
        fields = ('id', 'text', 'movie')
