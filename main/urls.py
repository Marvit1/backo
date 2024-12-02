from django.urls import path, include
from rest_framework import routers

from main import views

router = routers.SimpleRouter()
router.register(r'main-post', views.MainPost)
router.register(r'youtube', views.VideoViewSet)

router.register(r'top-viewed-posts', views.TopViewedPostsViewSet, basename='top-viewed-posts')



post_detail = views.MainPostDetailViewset.as_view({'get': 'retrieve'})
video_detail = views.VideoDetail.as_view({'get': 'retrieve'})
urlpatterns = [
    path('', include(router.urls)),
    
    path('latest-post/', views.MainPostList.as_view({'get': 'list'}), name='latest-post'),
    path('pol-col/', views.MainPolit.as_view({'get': 'list'}), name='pol-col'),
    path('sport/', views.MainSport.as_view({'get': 'list'}), name='sport'),
    path('media/', views.MainMedia.as_view({'get': 'list'}), name='media'),
    path('analytical/', views.MainAnalit.as_view({'get': 'list'}), name='analytical'),
    path('youtube/<int:pk>/', views.VideoYDetailY.as_view(), name='video-detailY'),
    path('search-posts/', views.SearchPosts.as_view(), name='search-posts'),
    path('latest-video/', views.VideoList.as_view({'get': 'list'}), name='video-list'),
    path('section/', views.SectionList.as_view({'get': 'list'}),  name='section'),
    path('category/', views.CategoryList.as_view(),  name='category'),
    path('post/<int:pk>/', post_detail, name='mainpost-detail'),    
    path('video/<int:pk>/', video_detail, name='video-detail'),

    path('video-emb/', views.VideoViewSeti.as_view({'get': 'list'}), name='embed'),

    path('reclam/', views.ReclamPost.as_view({'get': 'list'}), name="reclam"),

]