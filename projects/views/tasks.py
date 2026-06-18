from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from projects.models import Task
from projects.serializers import (
    TaskDetailSerializer,
    TaskUpdateSerializer,
    AllTasksSerializer,
    CreateTaskSerializer
)


class TaskViewSet(ModelViewSet):

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'priority', 'project', 'assignee']
    search_fields = ['name']

    def get_queryset(self):
        queryset = Task.objects.all()

        return queryset

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return TaskUpdateSerializer
        elif self.action == 'retrieve':
            return TaskDetailSerializer

'''Напишите класс-отображение AllTasksListAPIView для получения списка всех задач, 
привязанных к конкретному проекту, или сотруднику на выбор. Реализуйте пагинацию для отображения
 только первых пяти записей на одной странице. Добавьте метод post для создания задачи.
Зарегистрируйте новый эндпоинт, проверьте как отрабатывают запросы GET, POST.'''

class AllTasksListApiView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['project', 'assignee']

    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return  AllTasksSerializer
        return CreateTaskSerializer


