from django.contrib import admin
from movie.models import Director, Movie, Review


# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'director')
    list_display_links = ('title', 'director')
    search_fields = ('title', 'director')


admin.site.register(Director)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)
