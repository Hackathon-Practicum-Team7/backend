from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.about.selectors import get_cities, get_direction_of_study
from apps.api.v1.serializers.about import (DirectionOfSudySerialiser,
                                           InfoOutputSerializer)


@extend_schema_view(get=extend_schema(auth=[], tags=["auxilary"]))
class CityView(generics.ListAPIView):
    """
    View для отдачи списка городов
    """

    serializer_class = InfoOutputSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = get_cities()
        return queryset


@extend_schema_view(get=extend_schema(auth=[], tags=["auxilary"]))
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
