from django.contrib import admin
from .models import Comment, Movie, Director


admin.site.register(Comment)
admin.site.register(Movie)


class MovieInline(admin.TabularInline):
	model = Movie
	extra = -1

@admin.register(Director)
class Director(admin.ModelAdmin):
	list_display = ('name',)
	inlines = [MovieInline]