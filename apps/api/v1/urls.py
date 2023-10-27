from django.urls import include, path

from apps.api.v1.views.about import CityView, ProfessionView
from apps.api.v1.views.card import StudentCardView
from apps.api.v1.views.favorite import FavoritesView
from apps.api.v1.views.resume import DownloadResumeView
from apps.api.v1.views.students_list import StudentListView

urlpatterns = [
    # Авторизация
    path('auth/', include('djoser.urls.jwt')),
    # Скачать резюме
    path(
        'students/<uuid:id>/download_resume/',
        DownloadResumeView.as_view(),
        name='download_resume'
    ),
    # Добавить в избранное
    path(
        'students/favorite/',
        FavoritesView.as_view(),
        name='favorite-students'),
    # Карточка студента
    path('students/<uuid:id>/', StudentCardView.as_view(), name='student'),
    # Список студентов
    path('students/', StudentListView.as_view(), name='student-list'),
    # Вспомогательные поинты
    path('cities/', CityView.as_view(), name='cities'),
    path('professions/', ProfessionView.as_view(), name='professions'),
]
