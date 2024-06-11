from home.models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class blogserializer(serializers.ModelSerializer):

    class Meta:
        model=blog
        fields="__all__"
        

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']
    
    def create(self, validated_data):
        username=validated_data['username']
        password=validated_data['password']
        user=User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return user
    



