from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.recruiters.models import Favorite
from apps.students.models import Student
from apps.api.v1.serializers.card import StudentCardSerializer


class FavoritesView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=["post", "delete"])
    def favorite(self, request, id):
        student = get_object_or_404(Student, id=id)
        if request.method == "POST":
            try:
                Favorite.objects.create(
                    recruiter=request.user, student=student)
            except IntegrityError:
                return Response(data={"detail": "Студент уже в избранном."},
                                status=status.HTTP_400_BAD_REQUEST)
            serializer = StudentCardSerializer(
                student, context={"request": request})
            return Response(
                data=serializer.data, status=status.HTTP_201_CREATED)
        deleted, _ = Favorite.objects.filter(
            recruiter=request.user, student=student).delete()
        if deleted:
            return Response({"message": "Студент удален из избранного"},
                            status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "Студент не найден в избранном"},
                            status=status.HTTP_404_NOT_FOUND)
