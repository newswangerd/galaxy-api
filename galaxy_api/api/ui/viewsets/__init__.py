from .namespace import NamespaceViewSet, MyNamespaceViewSet
from .collection import CollectionViewSet, CollectionVersionViewSet, CollectionImportViewSet
from .tags import TagsViewSet
from .me import MeViewSet

__all__ = (
    'NamespaceViewSet',
    'MyNamespaceViewSet',
    'CollectionViewSet',
    'CollectionVersionViewSet',
    'CollectionImportViewSet',
    'TagsViewSet',
    'MeViewSet'
)
