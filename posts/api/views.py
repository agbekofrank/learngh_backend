from rest_framework import generics
from posts.models import PostInstance, Like
from .serializers import PostInstanceSerializer
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response



class AddPost(generics.CreateAPIView):

    queryset = PostInstance.objects.all()
    serializer_class = PostInstanceSerializer


# class RetrieveUpdatePost(generics.RetrieveUpdateAPIView):
#     queryset = PostInstance.objects.all()
#     serializer_class = PostInstanceSerializer

class RetrieveUpdateDeletePost(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostInstance.objects.all()
    serializer_class = PostInstanceSerializer


class ListPost(generics.ListAPIView):
    queryset = PostInstance.objects.all()
    serializer_class = PostInstanceSerializer


@api_view
def like(request):
	post_id = request.GET.get("likeId", "")
	user = request.user
	post = PostInstance.objects.get(pk=post_id)
	liked= False
	like = Like.objects.filter(user=user, post=post)
	if like:
		like.delete()
	else:
		liked = True
		Like.objects.create(user=user, post=post)
	resp = {
        'liked':liked
    }
	response = json.dumps(resp)
	return Response(response, content_type = "application/json")