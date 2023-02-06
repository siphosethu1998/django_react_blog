from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer

@api_view(["GET"])
def blog_list(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)

    return Response(serializer.data)

@api_view(["GET"])
def blog_detail(request, id):
    blog = Blog.objects.get(pk=id)
    serializer = BlogSerializer(blog, many=False)

    return Response(serializer.data)

@api_view(["POST"])
def blog_create(request):
    serializer = BlogSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
