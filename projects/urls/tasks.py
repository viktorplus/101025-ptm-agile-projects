from django.urls import path
from rest_framework.routers import DefaultRouter

from projects.views.projects import ProjectsListAPIView
from projects.views.tasks import TaskViewSet, AllTasksListApiView


# router = DefaultRouter()
# router.register('', TaskViewSet, basename='tasks')

urlpatterns = [path('', AllTasksListApiView.as_view())]
# urlpatterns += router.urls
