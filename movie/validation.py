from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from movie.models import Director, Movie, Review


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=3, max_length=100)


class DirectorCreateSerializer(DirectorValidateSerializer):
    def validate_name(self, name):
        if Director.objects.filter(name=name).count() > 0:
            raise ValidationError('Name must be unique')
        return name


class DirectorUpdateSerializer(DirectorValidateSerializer):
    def validate_name(self, name):
        if Director.objects.filter(name=name).exclude(id=self.context.get('id')).count() > 0:
            raise ValidationError('Name must be unique')
        return name


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=3, max_length=80)
    description = serializers.CharField()
    duration = serializers.IntegerField(required=False, min_value=1)
    director = serializers.IntegerField(required=False, min_value=1)

    def valid_director(self, director):
        try:
            Director.objects.get(id=director)
        except Director.DoesNotExist:
            raise ValidationError('Director not found')
        return director


class MovieCreateSerializer(MovieValidateSerializer):
    def validate_title(self, title):
        if Movie.objects.filter(title=title).count() > 0:
            raise ValidationError('title must be unique')
        return title


class MovieUpdateSerializer(MovieValidateSerializer):
    def validate_title(self, title):
        if Movie.objects.filter(title=title).exclude(id=self.context.get('id')).count() > 0:
            raise ValidationError('title must be unique')
        return title


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=False, min_length=3)
    movie = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField(min_value=1, max_value=5)

    def validate_movie(self, movie):
        try:
            Movie.objects.get(id=movie)
        except Movie.DoesNotExist:
            raise ValidationError('Movie not found')
        return movie
