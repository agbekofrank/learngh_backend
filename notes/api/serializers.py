from rest_framework import serializers
from notes.models import NoteInstance

class NoteInstanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoteInstance
        fields = '__all__'
