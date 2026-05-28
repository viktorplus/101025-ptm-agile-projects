"""Напишите функцию, которая будет обрабатывать GET запросы для получения списка всех проектов из Базы данных.
Зарегистрировать эту функцию в списке эндпоинтов в файле urls.py"""
from django.db.migrations import serializer
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from projects.models import Project, project
from projects.serializers.projects import ProjectListSerializer

@api_view(["GET"])
def get_all_projects(request):
    projects=Project.objects.all()
    serializer = ProjectListSerializer(projects, many=True)
    return Response(serializer.data)

