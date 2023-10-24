from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.api.v1.filters import StudentFilter
from apps.api.v1.serializers.students_list import StudentListSerializer
from apps.students.models import Student


class StudentListView(generics.ListAPIView):
    """View для получения списка студентов."""
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StudentFilter
