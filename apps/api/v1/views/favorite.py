from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.api.v1.serializers.students_list import StudentIDListSerializer
from apps.students.selectors import get_selected_students


@extend_schema_view(
    post=extend_schema(
        request=StudentIDListSerializer,
        responses={201: None},
        description="Добавление студентов в избранное"
    ),
    delete=extend_schema(
        request=StudentIDListSerializer,
        responses={204: None},
        description="Request body точно такое же как и для метода POST"
    )
)
class FavoritesView(views.APIView):
    """View для добавления студента в избранное."""
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        students_id = request.data.get("students_id")
        queryset = get_selected_students(students_id)
        request.user.favorite_students.add(*queryset)
        return Response(
            {"message": "Студенты успешно добавлены в избранное"},
            status=status.HTTP_201_CREATED)

    def delete(self, request):
        students_id = request.data.get("students_id")
        queryset = get_selected_students(students_id)
        request.user.favorite_students.remove(*queryset)
        return Response(
            {"message": "Студенты успешно удалены из избранного"},
            status=status.HTTP_204_NO_CONTENT
        )
