from rest_framework import serializers

from .models import Category, Main, Video, VideoY, Item, Reclam

class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = (
            "id",
            "name",
            "text",
            "get_absolute_url",
            "get_image",
            "get_thumbnail",
            "date_added", 
            "view_count",
            "published",
            "link_name",
            "link",
        )

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = (
            "id",
            "name",
            "description",
            "get_absolute_url",
            "get_video_url",
            "get_thumbnail_url",
            "date_added", 
            "view_count",
            'published',
            
        )       

# serializers.py


class VideoSerializerY(serializers.ModelSerializer):
    class Meta:
        model = VideoY
        fields = ('id', 
                  'title',
                  'youtube_id',
                    'description', 
                    'published_at',
                    "get_absolute_url",
            "get_video_url",
            )

class VideoSerializerI(serializers.ModelSerializer):
   class Meta:
      model = Item
      fields = ('video',)

      #Reclam
class ReclamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reclam
        fields = '__all__'