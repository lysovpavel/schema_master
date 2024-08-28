from rest_framework.routers import DefaultRouter

from elements.viewsets.arrow import ArrowViewSet
from elements.viewsets.block import BlockViewSet

elements_router = DefaultRouter()
elements_router.register(r'arrow', ArrowViewSet, basename='arrow')
elements_router.register(r'block', BlockViewSet, basename='block')
