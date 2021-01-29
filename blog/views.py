from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status


from blog.models import Post, Comment
from blog.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer