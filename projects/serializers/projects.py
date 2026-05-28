from rest_framework import serializers
from projects.models import Project

'''Напишите первый сериализатор, который будет обрабатывать поля id и name для 
проекта, выдавая общую базу для вывода всех проектов.'''

class ProjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ["id", "name"]


