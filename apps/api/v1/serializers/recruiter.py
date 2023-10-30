from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer

User = get_user_model()


class RecruiterSerializer(UserSerializer):
    """Сериализатор для users/me"""

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'name',
            'surname',
            'avatar',
            'company',
            'favorite_students',
        )
