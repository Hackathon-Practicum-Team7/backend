from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.api.v1.serializers.card import StudentCardSerializer
from apps.students.selectors import get_student


class StudentCardView(generics.RetrieveAPIView):
    """View для отдачи карточки студента"""

    serializer_class = StudentCardSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return get_student(self.kwargs.get("id"))
