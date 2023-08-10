from rest_framework import generics
from posts.models import PostInstance
from .serializers import PostInstanceSerializer



class AddPost(generics.CreateAPIView):

    queryset = PostInstance.objects.all()
    serializer_class = PostInstanceSerializer


class RetrieveUpdatePost(generics.RetrieveUpdateAPIView):
    queryset = PostInstance.objects.all()
    serializer_class = PostInstanceSerializer


class ListPost(generics.ListAPIView):
    queryset = PostInstance.objects.all()
    serializer_class = PostInstanceSerializer