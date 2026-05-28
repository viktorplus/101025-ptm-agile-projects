from django.db.migrations import serializer
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from projects.models import Tag

from projects.models import Project, project
from projects.serializers.tags import TagListSerializer

@api_view(["GET"])
def get_list_tags(request):
    tags=Tag.objects.all()
    serializer = TagListSerializer(tags, many=True)
    return Response(serializer.data)