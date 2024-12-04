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
    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        # Ensure URLs use HTTPS
        if 'get_image' in data and data['get_image']:
            data['get_image'] = data['get_image'].replace("http://", "https://")
        
        if 'get_thumbnail' in data and data['get_thumbnail']:
            data['get_thumbnail'] = data['get_thumbnail'].replace("http://", "https://")
        
        return data

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
    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        # Ensure URLs use HTTPS
        if 'get_video_url' in data and data['get_video_url']:
            data['get_video_url'] = data['get_video_url'].replace("http://", "https://")
        
        return data

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
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        # Assuming you have URLs in the model fields (like get_image)
        # Replace http with https in URLs if any
        if 'get_image' in data and data['get_image']:
            data['get_image'] = data['get_image'].replace("http://", "https://")
        
        return data