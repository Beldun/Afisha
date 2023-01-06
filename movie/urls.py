from django.urls import path
from movie.views import DirectorView, DirectorDetailView, MovieView, MovieDetailView, \
    ReviewView, ReviewDetailView, ReviewMovieView

urlpatterns = [
    path('movies/', MovieView.as_view()),
    path('movies/<int:id>/', MovieDetailView.as_view()),
    path('directors/', DirectorView.as_view()),
    path('directors/<int:id>/', DirectorDetailView.as_view()),
    path('reviews/', ReviewView.as_view()),
    path('reviews/<int:id>/', ReviewDetailView.as_view()),
    path('movies/reviews/', ReviewMovieView.as_view())
]
