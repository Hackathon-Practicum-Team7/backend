from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.api.v1.filters import StudentFilter
from apps.api.v1.serializers.students_list import StudentListSerializer
from apps.students.selectors import get_all_students


class StudentListView(generics.ListAPIView):
    """View для получения списка студентов."""
    serializer_class = StudentListSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StudentFilter

    def get_queryset(self):
        skills = self.request.query_params.getlist("skills")
        queryset = get_all_students(skills)
        return queryset
