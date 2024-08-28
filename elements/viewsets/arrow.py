from elements.models import Arrow
from rest_framework import viewsets

from elements.serializers.arrow import ArrowSerializer


class ArrowViewSet(viewsets.ModelViewSet):
    serializer_class = ArrowSerializer
    queryset = Arrow.objects.all()
