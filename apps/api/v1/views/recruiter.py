from django.contrib.auth import get_user_model
from djoser.conf import settings
from djoser.views import UserViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.decorators import action


User = get_user_model()


@extend_schema_view(
    list=extend_schema(exclude=True),
    retrieve=extend_schema(exclude=True),
    create=extend_schema(exclude=True),
    update=extend_schema(exclude=True),
    partial_update=extend_schema(exclude=True),
    destroy=extend_schema(exclude=True),
    activation=extend_schema(exclude=True),
    resend_activation=extend_schema(exclude=True),
    reset_username=extend_schema(exclude=True),
    reset_username_confirm=extend_schema(exclude=True),
    reset_password=extend_schema(exclude=True),
    set_username=extend_schema(exclude=True),
    set_password=extend_schema(exclude=True),
    reset_password_confirm=extend_schema(exclude=True),
)
class RecruiterViewSet(UserViewSet):
    permission_classes = settings.PERMISSIONS.user
    allowed_methods = ('get',)

    @action(["get"], detail=False)
    def me(self, request, *args, **kwargs):
        self.get_object = self.get_instance
        if request.method == "GET":
            return self.retrieve(request, *args, **kwargs)
