from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GenreViewSet, LanguageViewSet, CountryViewSet,
    MovieViewSet, CommentViewSet, Register_api
)

router = DefaultRouter()
router.register(r'genres', GenreViewSet)
router.register(r'languages', LanguageViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'register', Register_api, basename='register')

urlpatterns = [
    path('', include(router.urls)),
]
