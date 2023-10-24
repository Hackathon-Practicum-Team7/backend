from django.urls import include, path

from apps.api.v1.views.about import CityView, ProfessionView


urlpatterns = [
    # Авторизация
    path('auth/', include('djoser.urls.jwt')),
    # Вспомогательные поинты
    path('cities/', CityView.as_view(), name='cities'),
    path('professions/', ProfessionView.as_view(), name='professions'),
]
