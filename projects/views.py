from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import ProjectCategorySerializer, ProjectCharacteristicSerializer, ProjectSerializer
from .models import Project, ProjectCategory, ProjectCharacteristic

class ProjectCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
    def list(self, request):
        queryset = ProjectCategory.objects.all()
        serializer = ProjectCategorySerializer(queryset, many=True)
        return Response(serializer.data)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'category'
    def list(self, request):
        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, category=None):
        queryset = Project.objects.filter(category_id=category)
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

class ProjectCharacteristicViewSet(viewsets.ModelViewSet):
    queryset = ProjectCharacteristic.objects.all()
    serializer_class = ProjectCharacteristicSerializer
    lookup_field = 'project'
    def retrieve(self, request, project=None):
        queryset = ProjectCharacteristic.objects.filter(project_id=project)
        serializer = ProjectCharacteristicSerializer(queryset, many=True)
        return Response(serializer.data)