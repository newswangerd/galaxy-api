from django.urls import path, include
from rest_framework import routers

from . import viewsets


router = routers.SimpleRouter()
router.register('namespaces', viewsets.NamespaceViewSet, basename='namespaces')
router.register('my-namespaces', viewsets.MyNamespaceViewSet, basename='my-namespaces')
router.register('collections', viewsets.CollectionViewSet, basename='collections')
router.register('collection-versions',
                viewsets.CollectionVersionViewSet, basename='collection-versions')
router.register('all-collection-versions',
                viewsets.FullCollectionVersionViewSet, basename='all-collection-versions')
router.register(
    'imports/collections',
    viewsets.CollectionImportViewSet,
    basename='collection-imports',
)
router.register('tags', viewsets.TagsViewSet, basename='tags')

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
]
