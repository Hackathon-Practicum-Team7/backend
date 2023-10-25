from django.urls import include, path

from apps.api.v1.views.about import CityView, ProfessionView
from apps.api.v1.views.card import StudentCardView
from apps.api.v1.views.favorite import FavoritesView
from apps.api.v1.views.students_list import StudentListView
from apps.api.v1.views.resume import DownloadResumeView

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
        'students/<uuid:id>/favorite/',
        FavoritesView.as_view({'post': 'favorite', 'delete': 'favorite'}),
        name='student-favorite'),
    # Карточка студента
    path('students/<uuid:id>/', StudentCardView.as_view(), name='student'),
    # Список студентов
    path('students/', StudentListView.as_view(), name='student-list'),
    # Вспомогательные поинты
    path('cities/', CityView.as_view(), name='cities'),
    path('professions/', ProfessionView.as_view(), name='professions'),
]
