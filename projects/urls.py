from django.http import HttpResponse
from django.urls import path

from projects.views.projects import get_all_projects

from projects.views.tasks import get_list_task
from projects.views.tags import get_list_tags


urlpatterns = [
    path('', lambda request: HttpResponse('hello')),
    path('projects/',get_all_projects),
    path('tasks/',get_list_task),
    path('tags/', get_list_tags),


]
