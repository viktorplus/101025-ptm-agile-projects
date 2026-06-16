from datetime import datetime

from django.utils import timezone
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from projects.models import Project
from projects.serializers import ProjectListSerializer, CreateProjectSerializer, ProjectDetailSerializer


class ProjectsListAPIView(APIView):
    def get_objects(self):
        queryset = Project.objects.all()

        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')

        if date_from:
            date_from = timezone.make_aware(
               datetime.strptime(date_from, '%Y-%m-%d')
            )

            queryset = queryset.filter(
               created_at__gte=date_from
            )

        if date_to:
            date_to = timezone.make_aware(
                datetime.strptime(date_to, '%Y-%m-%d')
            ) if date_from else timezone.now().strftime('%Y-%m-%d')

            queryset = queryset.filter(
                created_at__lte=date_to
            )

        return queryset

    def get(self, request: Request) -> Response:
        projects = self.get_objects()

        if not projects.exists():
            return Response(
               data=[],
               status=status.HTTP_204_NO_CONTENT
            )

        serializer = ProjectListSerializer(projects, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def post(self, request: Request) -> Response:
        serializer = CreateProjectSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
               serializer.validated_data,
               status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

"""Напишите новый класс-отображение ProjectDetailAPIView для получения конкретного проекта, 
обновления и удаления проекта.
При обновлении полученного проекта добавьте возможность частичного обновления полей.
Зарегистрируйте новый эндпоинт, проверьте как отрабатывают запросы GET, PUT, DELETE.
Зафиксируйте все изменения, сделайте запрос на слияние."""
class ProjectDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
