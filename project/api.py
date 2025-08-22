from .models import Project
from rest_framework import viewsets, filters
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by("-createdAt")
    serializer_class = ProjectSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['brand', 'holder', 'status']
    ordering_fields = ['createdAt', 'updateAt']