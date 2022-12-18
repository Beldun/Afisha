from django.contrib import admin
from movie.models import Director, Movie, Review


# Register your models here.

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'director')
    list_display_links = ('title',)
    search_fields = ('title', 'director')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'stars', 'created_date', 'modified_date')
    list_display_links = ('movie',)
    search_fields = ('stars', )


admin.site.register(Director, DirectorAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
