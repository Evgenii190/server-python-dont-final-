from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import BlogCategorySerializer, BlogPostSerializer

from .models import BlogCategory, BlogPost

class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    def list(self, request):
        queryset = BlogCategory.objects.all()
        serializer = BlogCategorySerializer(queryset, many=True)
        return Response(serializer.data)

class BlogPostByCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'category'
    def list(self, request):
        queryset = BlogPost.objects.all()
        serializer = BlogPostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, category=None):
        queryset = BlogPost.objects.filter(category_id=category)
        serializer = BlogPostSerializer(queryset, many=True)
        return Response(serializer.data)

class BlogPostBySlugViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    def list(self, request):
        queryset = BlogPost.objects.order_by("-id")[0:3]
        serializer = BlogPostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, slug=None):
        queryset = BlogPost.objects.filter(slug=slug)
        serializer = BlogPostSerializer(queryset, many=True)
        return Response(serializer.data)
    


    
