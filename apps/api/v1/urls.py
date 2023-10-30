from django.urls import include, path
from rest_framework import routers

from apps.api.v1.views.auxiliary import (CityView, ExportExcelView,
                                         ProfessionView, SkillView)
from apps.api.v1.views.card import StudentCardView
from apps.api.v1.views.favorite import FavoritesView
from apps.api.v1.views.recruiter import RecruiterViewSet
from apps.api.v1.views.resume import DownloadResumeView
from apps.api.v1.views.students_list import StudentListView

router = routers.DefaultRouter()
router.register("users", RecruiterViewSet)

urlpatterns = [
    # Авторизация
    path("auth/", include("djoser.urls.jwt")),
    # Текущий юзер
    path('auth/', include(router.urls)),
    # Эндпоинты на студентов
    path(
        "students/<uuid:id>/download_resume/",
        DownloadResumeView.as_view(),
        name="download_resume",
    ),
    path(
        "students/favorite/", FavoritesView.as_view(), name="favorite-students"
    ),
    path("students/<uuid:id>/", StudentCardView.as_view(), name="student"),
    path("students/", StudentListView.as_view(), name="student-list"),
    # Вспомогательные поинты
    path("cities/", CityView.as_view(), name="cities"),
    path("professions/", ProfessionView.as_view(), name="professions"),
    path("skills/", SkillView.as_view(), name="skills"),
    # Скачивание файлов
    path("download/excel/", ExportExcelView.as_view(), name="download_excel"),
]
