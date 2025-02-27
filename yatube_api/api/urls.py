from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (
    FollowViewSet,
    GroupViewSet,
    CommentViewSet,
    PostViewSet
)
router = SimpleRouter()

router.register(r'follow', FollowViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts/(?P<post_id>[\d]+)/comments', CommentViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
