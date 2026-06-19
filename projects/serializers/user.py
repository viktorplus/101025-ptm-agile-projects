from rest_framework import serializers

from projects.models import User

# Создайте сериализатор UserListSerialzier для отображения только лишь некоторых
#  полей для пользователя:
# first_name
# last_name
# position
# email
# phone
# last_login




class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name",
 "last_name",  "role", "phone", "last_login")


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ("id", "date_joined", "last_login", "is_active")
        exclude = ("password", "is_superuser", "is_staff", "user_permissions", "groups")






