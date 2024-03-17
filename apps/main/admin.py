from django.contrib import admin

from apps.main.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
	fields = ['image', 'description', 'show']
	list_display = ['description', 'show']