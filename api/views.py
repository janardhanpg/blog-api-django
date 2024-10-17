from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer

# API Overview
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': 'api/blog-list/',
        'Details View': 'api/blog-details/<str:pk>',
        "Create": 'api/blog-create/',
        'Update': 'api/blog-update/<str:pk>',
        'Delete': 'api/blog-delete/<str:pk>/'
    }
    return Response(api_urls)

# List all blogs
@api_view(['GET'])
def blogList(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Get details of a specific blog
@api_view(['GET'])
def blogDetails(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Create a new blog
@api_view(['POST'])
def createBlog(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update an existing blog
@api_view(['PUT', 'PATCH'])
def updateBlog(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    serializer = BlogSerializer(instance=blog, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete a blog
@api_view(['DELETE'])
def deleteBlog(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    blog.delete()
    return Response(f"Blog with ID {pk} has been deleted", status=status.HTTP_204_NO_CONTENT)
