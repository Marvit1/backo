from django.contrib import admin
from embed_video.admin import AdminVideoMixin

from .models import Category, Main, Video, VideoY, Item, Reclam

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)

@admin.register(Main)
class NewsAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'name', 'date_added','view_count', 'published', 'link_name', 'link')
    list_display_links = ('id', 'name', 'view_count', 'published', 'link', 'link_name')
    list_per_page = 10
    search_fields = ['name', 'date_added',  'category__name','view_count', 'published']
    list_filter = ['category__name', 'view_count', 'published']
@admin.register(Category)
class CatsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_per_page = 10 
    
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_added', 'view_count', 'published')
    list_display_links = ('id', 'name', 'date_added', 'view_count', 'published')
    list_per_page = 10
    search_fields = ['name', 'date_added', 'view_count', 'published']


@admin.register(VideoY)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'youtube_id')
    list_display_links = ('id', 'title', 'youtube_id', 'description')
    list_per_page = 10
    search_fields = ['title', 'published_at','youtube_id']

@admin.register(Reclam)
class ReclamAdmin(admin.ModelAdmin):
    list_display = ('category', 'image', 'thumbnail', 'published', 'link', 'order')
    list_filter = ('published', 'category')
    search_fields = ('link', 'category__slug', 'slug')
    ordering = ('order', '-published',)
#admin.site.register(Category)
#admin.site.register(Main, NewsAdmin)
#admin.site.register(Video)

