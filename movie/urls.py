from django.urls import path
from movie.views import director_view, director_detail_view, movie_view, movie_detail_view, \
    review_view, review_detail_view, movie_review_detail

urlpatterns = [
    path('movies/', movie_view),
    path('movies/<int:id>/', movie_detail_view),
    path('directors/', director_view),
    path('directors/<int:id>/', director_detail_view),
    path('reviews/', review_view),
    path('reviews/<int:id>/', review_detail_view),
    path('movies/reviews/', movie_review_detail)
]
