from rest_framework import serializers

from apps.recruiters.models import Favorite
from .card import StudentCardSerializer


class FavoriteSerializer(serializers.ModelSerializer):
    """Сериализатор для добавления студента в избранное."""
    class Meta:
        model = Favorite
        fields = "__all__"

    def to_representation(self, instance):
        return StudentCardSerializer(instance, context={
            "request": self.context.get("request")
        }).data
