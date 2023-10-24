from django.urls import include, path

from apps.api.v1.views.about import CityView, ProfessionView
from apps.api.v1.views.card import StudentCardView


urlpatterns = [
    # Авторизация
    path('auth/', include('djoser.urls.jwt')),
    # Карточка студента
    path('students/<uuid:id>/', StudentCardView.as_view(), name='student'),
    # Вспомогательные поинты
    path('cities/', CityView.as_view(), name='cities'),
    path('professions/', ProfessionView.as_view(), name='professions'),
]
