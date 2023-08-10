from rest_framework import serializers
from users.models import UserInstance

class UserInstanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInstance
        fields = '__all__'