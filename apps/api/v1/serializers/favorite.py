# from rest_framework import serializers


# class FavoriteSerializer(serializers.Serializer):
#     students_id = serializers.ListField(
#         child=serializers.DictField(
#             child=serializers.UUIDField(
#                 format='hex_verbose',
#                 error_messages={'invalid': 'Invalid UUID format'},
#             ),
#         )
#     )
