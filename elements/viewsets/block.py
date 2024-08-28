from elements.models import Block
from rest_framework import viewsets

from elements.serializers.block import BlockSerializer


class BlockViewSet(viewsets.ModelViewSet):
    serializer_class = BlockSerializer
    queryset = Block.objects.all()
