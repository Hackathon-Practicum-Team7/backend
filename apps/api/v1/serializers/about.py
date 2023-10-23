from rest_framework import serializers


class InfoOutputSerializer(serializers.Serializer):
    """
    Сериализатор для моделей City, Profession
    """
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
