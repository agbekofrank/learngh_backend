
from rest_framework import generics
from users.models import UserInstance
from .serializers import UserInstanceSerializer

class UsersListView(generics.ListAPIView):
    queryset = UserInstance.objects.all()
    serializer_class = UserInstanceSerializer


class UserAddView(generics.CreateAPIView):

    queryset = UserInstance.objects.all()
    serializer_class = UserInstanceSerializer