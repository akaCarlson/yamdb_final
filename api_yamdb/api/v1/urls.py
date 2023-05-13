from django.urls import include, path
from rest_framework import routers

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    GetTokenView, ReviewViewSet, TitleViewSet,
                    UserSignupView, UserViewset)

router_api_v1 = routers.DefaultRouter()

router_api_v1.register('users', UserViewset)
router_api_v1.register('titles', TitleViewSet, basename='titles')
router_api_v1.register('genres', GenreViewSet, basename='genres')
router_api_v1.register(
    'categories', CategoryViewSet, basename='categories')
router_api_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_api_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

auth_patterns = [
    path('signup/', UserSignupView.as_view(), name='user_register'),
    path('token/',
         GetTokenView.as_view(),
         name='sliding_toket_obtain'),
]

urlpatterns = [
    path('', include(router_api_v1.urls)),
    path('auth/', include(auth_patterns)),
]
