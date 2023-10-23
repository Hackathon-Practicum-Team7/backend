from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.about.selectors import get_cities, get_direction_of_study
from apps.api.v1.serializers.about import (
    InfoOutputSerializer,
    DirectionOfSudySerialiser,
)


class CityView(generics.ListAPIView):
    """
    View для отдачи списка городов
    """
    serializer_class = InfoOutputSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = get_cities()
        return queryset


class ProfessionView(generics.ListAPIView):
    """
    View для отдачи списка направлений обучения и профессий, относящихся
    к этим направлениям
    """
    serializer_class = DirectionOfSudySerialiser
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = get_direction_of_study()
        return queryset
