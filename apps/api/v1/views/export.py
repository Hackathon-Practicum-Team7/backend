import pandas as pd
from io import BytesIO

from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.students.selectors import get_selected_students
from apps.students.utils import get_dataframe


class ExportExcelView(APIView):
    """View для скачивание файла excel"""

    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        studen = [
            {"id": "cd72cb18-3d90-43b0-9e32-ac91a7fceaa4"},
            {"id": "35ce3300-9c12-40b6-93ce-c03b7548200d"},
            {"id": "35ce3300-9c12-50b6-88ce-c03b8548200d"}
        ]
        students = get_selected_students(studen)
        # students = get_selected_students(request.data.get("students"))
        dataframe = get_dataframe(students)

        # with BytesIO() as b:
        #     with pd.ExcelWriter(b) as writer:
        #         dataframe.to_excel(
        #             writer, sheet_name="candidates", index=False
        #         )
        #         # workbook = writer.book
        #         # worksheet = writer.sheets['candidates']

        #         filename = "candidates.xlsx"

        #         res = HttpResponse(
        #             b.getvalue(),
        #             content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        #             # content_type='application/vnd.ms-excel'
        #         )
        #         res['Content-Disposition'] = 'attachment; filename="candidates.xlsx"'
        #         return res
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="candidates.xlsx"'

        with pd.ExcelWriter(response, engine="xlsxwriter") as writer:
            dataframe.to_excel(
                writer, sheet_name="candidates", index=False
            )
            workbook = writer.book
            worksheet = writer.sheets["candidates"]
            worksheet.set_zoom(90)
            total_fmt = workbook.add_format(
                {'align': 'right', 'bold': True, 'bottom': 6}
            )
            worksheet.set_column('A:B', 15)
            worksheet.set_column('C:D', 20)
            worksheet.set_column('E:E', 10)
            worksheet.set_column('F:F', 30)
            worksheet.set_column('G:G', 20)
            worksheet.set_column('H:I', 30)
        return response
