from django.db import models

from io import BytesIO
from PIL import Image
from django.core.files import File
from django.core.validators import FileExtensionValidator

from embed_video.fields import EmbedVideoField

class Item(models.Model):
    video = EmbedVideoField()

class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Անուն')
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Կատեգորիա'
        verbose_name_plural = 'Կատեգորիա'
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    

class Main(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    name = models.CharField(max_length=250, verbose_name='Վերնագիր')
    slug = models.SlugField()
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='նյութի ներբեռման ժամանակ')
    view_count = models.IntegerField(default=0)
    published = models.BooleanField(default=True, verbose_name='Գրառում հրապարակված է')
    link_name = models.CharField(max_length=250, verbose_name="Լինկի Վերնագիր", blank=True)
    link = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Հոդված'
        verbose_name_plural = 'Հոդված'
        ordering = ('-date_added',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
           return f'/{self.category.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
            
    def make_thumbnail(self, image, size=(800, 600)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thum_io = BytesIO()
        img.save(thum_io, 'JPEG', quality=105)

        thumbnail = File(thum_io, name=image.name)

        return thumbnail
            

class Video(models.Model):
    category = models.ForeignKey(Category, related_name='videos', on_delete=models.CASCADE)
    name = models.CharField(max_length=250, verbose_name='Անուն')
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    video_file = models.FileField(upload_to='uploads/videos/', validators=[FileExtensionValidator(['mp4', 'avi', 'mkv'])])
    thumbnail = models.ImageField(upload_to='uploads/thumbnails/', blank=True)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Ներբեռման ժամանակ')
    view_count = models.IntegerField(default=0)
    published = models.BooleanField(default=True, verbose_name='Գրառում հրապարակված է')

    class Meta:
        verbose_name = 'Տեսանյութներ'
        verbose_name_plural = 'Տեսանյութներ'
        ordering = ('-date_added',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_video_url(self):
        if self.video_file:
            return 'http://127.0.0.1:8000' + self.video_file.url
        return ''

    def get_thumbnail_url(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        return ''

        
class VideoY(models.Model):
    category = models.ForeignKey(Category, related_name='videoY', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    youtube_id = models.CharField(max_length=255)  # YouTube Video ID
    description = models.TextField(blank=True, null=True)
    published_at = models.DateTimeField()
    


    class Meta:
        verbose_name = 'Տեսանյութներ'
        verbose_name_plural = 'Տեսանյութներ'
        ordering = ('-published_at',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_video_url(self):
        if self.youtube_id:
            return 'http://127.0.0.1:8000' + self.youtube_id.url
        return ''

   

class Reclam(models.Model):
    category = models.ForeignKey(Category, related_name='reclam', on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='uploads/', blank=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True)
    published = models.BooleanField(default=True, verbose_name='Գրառում հրապարակված է')
    link = models.URLField(blank=True)
    slug = models.SlugField(default=1)
    order = models.PositiveIntegerField(default=0)  # Field to manage ordering

    class Meta:
        verbose_name = 'Գովազդ'
        verbose_name_plural = 'Գովազդ'
        ordering = ('order', '-published',)  # Order by 'order' first and then by 'published'

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return f'http://127.0.0.1:8000{self.image.url}'
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return f'http://127.0.0.1:8000{self.thumbnail.url}'
        elif self.image:
            self.thumbnail = self.make_thumbnail(self.image)
            self.save()
            return f'http://127.0.0.1:8000{self.thumbnail.url}'
        return ''
            
    def make_thumbnail(self, image, size=(800, 600)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)  # Use quality=85 for optimal compression
        
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail



