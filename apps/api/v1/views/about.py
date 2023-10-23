from rest_framework import generics
from rest_framework.permissions import AllowAny

# from apps.about.selectors import get_cities, get_professions
from apps.api.v1.serializers.about import InfoOutputSerializer


# TODO: сделать селекторы для получения кверисетов (сортировать по алфавиту)
class CityView(generics.ListAPIView):
    serializer_class = InfoOutputSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        # queryset = get_cities()
        return super().get_queryset()


class ProfessionView(generics.ListAPIView):
    serializer_class = InfoOutputSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        # queryset = get_professions()
        return super().get_queryset()
