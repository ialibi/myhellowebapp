from django.contrib import admin

# import your model
from collection.models import Song

#class SongAdmin(admin.ModelAdmin):
#	model = Song
#	list_display = ('name', 'description')
#	prepopulated_fields = {'slug': ('name',)}

#and register it
#admin.site.register(Song, SongAdmin)
admin.site.register(Song)