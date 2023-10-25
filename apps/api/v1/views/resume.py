from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.students.models import Student


class DownloadResumeView(APIView):
    ermission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        resume = get_object_or_404(Student, id=id).resume
        if resume:
            content_disposition = f'attachment; filename="{resume.name}"'
            response = FileResponse(
                resume.open('rb'), content_type='application/pdf')
            response['Content-Disposition'] = content_disposition
            return response
        return Response({'detail': 'Резюме не найдено.'},
                        status=status.HTTP_404_NOT_FOUND)
