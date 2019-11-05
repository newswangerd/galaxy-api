from .namespace import NamespaceViewSet, MyNamespaceViewSet
from .collection import (CollectionViewSet,
                         CollectionVersionViewSet,
                         FullCollectionVersionViewSet,
                         CollectionImportViewSet)
from .tags import TagsViewSet

__all__ = (
    'NamespaceViewSet',
    'MyNamespaceViewSet',
    'CollectionViewSet',
    'CollectionVersionViewSet',
    'FullCollectionVersionViewSet',
    'CollectionImportViewSet',
    'TagsViewSet',
)
