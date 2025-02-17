from django.contrib import admin
from .models import Genre, Language, Country, Movie, Comment
from django.utils.html import format_html



class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'view_movie_count')
    search_fields = ('name', 'description')
    list_filter = ('name',)

    def view_movie_count(self, obj):
        return f"{obj.movie_set.count()} movies"

    view_movie_count.short_description = 'Movie Count'



class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')



class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')



class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'language', 'country', 'description')
    search_fields = ('name', 'description', 'genre__name', 'language__name', 'country__name')
    list_filter = ('genre', 'language', 'country')
    ordering = ('name',)


    def get_thumbnail(self, obj):
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.video.url))

    get_thumbnail.short_description = 'Video Thumbnail'



class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'comment', 'created_at')
    search_fields = ('author__username', 'comment')
    list_filter = ('author', 'created_at')
    ordering = ('-created_at',)



admin.site.register(Genre, GenreAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment, CommentAdmin)
