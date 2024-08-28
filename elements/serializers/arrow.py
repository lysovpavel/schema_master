from rest_framework import serializers

from elements.models import Arrow


class ArrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arrow
        fields = '__all__'
