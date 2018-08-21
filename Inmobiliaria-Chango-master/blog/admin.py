from django.contrib import admin
from .models import Post, Property, PropertyImage

admin.site.register(Post)
# Register your models here.

class PropertyImageInline(admin.TabularInline):
	 model = PropertyImage
	 extra = 6

class PropertyAdmin(admin.ModelAdmin):
		inlines = [ PropertyImageInline ]

admin.site.register(Property, PropertyAdmin)