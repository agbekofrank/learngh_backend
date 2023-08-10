from rest_framework import generics
from notes.models import NoteInstance
from .serializers import NoteInstanceSerializer


# class Note(generics.ListCreateUpdateDestroy):
#     queryset = NoteInstance.objects.all()
#     serializer_class = NoteInstanceSerializer


class CreateNote(generics.CreateAPIView):

    queryset = NoteInstance.objects.all()
    serializer_class = NoteInstanceSerializer


class RetrieveNote(generics.RetrieveAPIView):
    queryset = NoteInstance.objects.all()
    serializer_class = NoteInstanceSerializer


class ListNote(generics.ListAPIView):
    queryset = NoteInstance.objects.all()
    serializer_class = NoteInstanceSerializer


class UpdateNote(generics.RetrieveUpdateAPIView):
    queryset = NoteInstance.objects.all()
    serializer_class = NoteInstanceSerializer


class DeleteNote(generics.DestroyAPIView):
    queryset = NoteInstance.objects.all()
    serializer_class = NoteInstanceSerializer
