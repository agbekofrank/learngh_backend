from rest_framework import serializers
from ..models import PostInstance

class PostInstanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostInstance
        fields = '__all__'
