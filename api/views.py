
from page.models import Profile, Page, Posts
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class PageList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = Page.objects.all()
    serializer_class = PagePublicSerializer



class PageDetais(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                generics.GenericAPIView):
    queryset = Page.objects.all


class PostList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostPublicSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



class PostsDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    generics.GenericAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostPublicSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)



class PostDetails(APIView):
    """"
    Get post INSTANCE by primary key
    """
    def get_object(self, pk):
        try:
            Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, formate=None):
        post = self.get_object(pk)
        serializers = PostPublicSerializer(post)
        return Response(serializers.data)
