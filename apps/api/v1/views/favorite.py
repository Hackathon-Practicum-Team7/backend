from rest_framework import status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# from apps.api.v1.serializers.favorite import FavoriteSerializer
from apps.students.selectors import get_selected_students


class FavoritesView(views.APIView):
    """View для добавления студента в избранное."""
    # serializer_class = FavoriteSerializer
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
