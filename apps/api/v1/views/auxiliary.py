import pandas as pd

from django.http import HttpResponse
from rest_framework import generics, views
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_spectacular.utils import extend_schema_view, extend_schema

from apps.about.selectors import get_cities, get_direction_of_study, get_all_skills
from apps.api.v1.serializers.auxiliary import (
    InfoOutputSerializer,
    DirectionOfSudySerialiser,
)
from apps.students.selectors import get_selected_students
from apps.students.utils import get_dataframe


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


@extend_schema_view(get=extend_schema(auth=[], tags=["auxilary"]))
class SkillView(generics.ListAPIView):
    """
    View для отдачи списка скиллов
    """

    serializer_class = InfoOutputSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = get_all_skills()
        return queryset


@extend_schema_view(post=extend_schema(tags=["auxilary"]))
class ExportExcelView(views.APIView):
    """View для скачивание файла excel"""

    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        students = get_selected_students(request.data.get("students"))
        dataframe = get_dataframe(students)

        filename = "candidates.xlsx"
        response = HttpResponse(content_type="application/vnd.ms-excel")
        response["Content-Disposition"] = f"attachment; filename={filename}"

        with pd.ExcelWriter(response, engine="xlsxwriter") as writer:
            dataframe.to_excel(writer, sheet_name="candidates", index=False)
            workbook = writer.book
            worksheet = writer.sheets["candidates"]
            worksheet.set_zoom(90)
            workbook.add_format({"align": "right", "bold": True, "bottom": 6})
            worksheet.set_column("A:A", 15)
            worksheet.set_column("B:C", 20)
            worksheet.set_column("D:D", 12)
            worksheet.set_column("E:E", 22)
            worksheet.set_column("F:F", 12)
            worksheet.set_column("G:H", 20)

        return response
