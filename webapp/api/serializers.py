from rest_framework import serializers
from .models import User
from .models import Forest
from .models import DiaryEntry



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ForestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forest
        fields = '__all__'   


class DiaryEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryEntry
        fields = '__all__'
            
