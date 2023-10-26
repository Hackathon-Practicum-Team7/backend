from django.urls import include, path

from apps.api.v1.views.auxiliary import (
    CityView,
    ProfessionView,
    ExportExcelView,
)
from apps.api.v1.views.card import StudentCardView
from apps.api.v1.views.students_list import StudentListView
from apps.api.v1.views.resume import DownloadResumeView

urlpatterns = [
    # Авторизация
    path('auth/', include('djoser.urls.jwt')),
    # Эндпоинты на студентов
    path(
        'students/<uuid:id>/download_resume/',
        DownloadResumeView.as_view(),
        name='download_resume'
    ),
    path('students/<uuid:id>/', StudentCardView.as_view(), name='student'),
    path('students/', StudentListView.as_view(), name='student-list'),
    # Вспомогательные поинты
    path('cities/', CityView.as_view(), name='cities'),
    path('professions/', ProfessionView.as_view(), name='professions'),
    # Скачивание файлов
    path('download/excel/', ExportExcelView.as_view(), name='download_excel'),
]
