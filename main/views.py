
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status
from .models import Video, VideoY, Item, Reclam
from .serializers import VideoSerializer, VideoSerializerY, VideoSerializerI, ReclamSerializer


from .models import Main, Category
from .serializers import MainSerializer

from rest_framework import viewsets, mixins



#Categoryia
class CategoryList(APIView):

    def get(self, request, format=None):
        products = Category.objects.all()
        serializer = MainSerializer(products, many=True)
        return Response(serializer.data)
    

#pordz visewtclass MainPost(viewsets.ReadOnlyModelViewSet):
class MainPost(viewsets.ReadOnlyModelViewSet):

    queryset = Main.objects.filter(published=True)[:150]
    serializer_class = MainSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        # Modify the image URLs to use https
        for obj in queryset:
            if hasattr(obj, 'get_image') and callable(obj.get_image):
                image_url = obj.get_image()
                if isinstance(image_url, str):
                    obj.get_image = image_url.replace("http://", "https://")

            if hasattr(obj, 'get_thumbnail') and callable(obj.get_thumbnail):
                thumbnail_url = obj.get_thumbnail()
                if isinstance(thumbnail_url, str):
                    obj.get_thumbnail = thumbnail_url.replace("http://", "https://")

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



#Main POSTS
class MainPostList(viewsets.ReadOnlyModelViewSet):
    serializer_class = MainSerializer

    def get_queryset(self):
        return Main.objects.filter(slug='econom', published=True).select_related('category')[:7]


#polit
class MainPolit(viewsets.ReadOnlyModelViewSet):
    serializer_class = MainSerializer

    def get_queryset(self):
        return Main.objects.filter(slug="pol", published=True).select_related('category')[:6]

#sport
class MainSport(viewsets.ReadOnlyModelViewSet):
    serializer_class = MainSerializer
    def get_queryset(self):
        return Main.objects.filter(slug="sport", published=True ).select_related('category')[:6]

#media
class MainMedia(viewsets.ReadOnlyModelViewSet):
    serializer_class = MainSerializer
    def get_queryset(self):
        return Main.objects.filter(slug="media", published=True).select_related('category')[:4]

#analiticl
class MainAnalit(viewsets.ReadOnlyModelViewSet):
    serializer_class = MainSerializer
    def get_queryset(self):
        return Main.objects.filter(slug="analytical", published=True).select_related('category')[:7]

#DETAILPAGE Main Post
class MainPostDetailViewset(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Main.objects.filter(published=True)
    serializer_class = MainSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_count += 1  # Increment the view count
        instance.save(update_fields=['view_count'])  # Save the updated view count
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
     
    # If you have any custom logic that you would need to run,
    # you can override the retrieve method. However, for most cases,
    # the default implementation provided by RetrieveModelMixin should suffice.

# video   
class VideoList(viewsets.ReadOnlyModelViewSet):
    queryset = Video.objects.filter(published=True).select_related('category')[:50]
    serializer_class = VideoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        # Replace 'http' with 'https' for video URLs
        for video in queryset:
            if hasattr(video, 'get_image') and callable(video.get_image):
                image_url = video.get_image()
                if isinstance(image_url, str):  # Check if it's a string
                    video.get_image = image_url.replace("http://", "https://")
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        # Replace 'http' with 'https' for video URLs
        if hasattr(instance, 'get_image') and callable(instance.get_image):
            image_url = instance.get_image()
            if isinstance(image_url, str):  # Check if it's a string
                instance.get_image = image_url.replace("http://", "https://")
        
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    
    
class VideoDetail(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Video.objects.filter(published=True)
    serializer_class = VideoSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_count += 1  # Increment the view count
        instance.save(update_fields=['view_count'])  # Save the updated view count
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

   
# Section
class SectionList(viewsets.ReadOnlyModelViewSet):
    queryset = Main.objects.all()
    serializer_class = MainSerializer

    def get_queryset(self):
        return Main.objects.filter(slug="section", published=True).select_related('category')[:1]

    


# Search

class SearchPosts(APIView):
    def get(self, request, format=None):
        query = self.request.GET.get('query', '')
        search_results = Main.objects.filter(Q(name__icontains=query) | Q(text__icontains=query), published=True)
        serializer = MainSerializer(search_results, many=True)
        return Response(serializer.data)
   











   
#youtube
class VideoViewSet(viewsets.ModelViewSet):
    queryset = VideoY.objects.all()
    serializer_class = VideoSerializerY
    

class VideoYDetailY(APIView):
    """
    Retrieve, update or delete a video instance.
    """
    def get_object(self, pk):
        try:
            return VideoY.objects.get(pk=pk)
        except VideoY.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        video = self.get_object(pk)
        serializer = VideoSerializerY(video)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        video = self.get_object(pk)
        serializer = VideoSerializerY(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        video = self.get_object(pk)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#top-viewed-posts
class TopViewedPostsViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        # Retrieve the top 10 most viewed posts
        top_posts = Main.objects.order_by('-view_count' )[:10]
        serializer = MainSerializer(top_posts, many=True)
        return Response(serializer.data)
    



class VideoViewSeti(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = VideoSerializerI


#Reclam
class ReclamPost(viewsets.ReadOnlyModelViewSet):
    queryset = Reclam.objects.filter(published=True).order_by('order')[:10]
    serializer_class = ReclamSerializer