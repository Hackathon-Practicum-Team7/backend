from rest_framework import serializers


class InfoOutputSerializer(serializers.Serializer):
    """
    Сериализатор для модели City
    """
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()


class DirectionOfSudySerialiser(InfoOutputSerializer):
    """
    Сериализатор для DirectionOf Study
    """
    professions = InfoOutputSerializer(many=True, read_only=True)
