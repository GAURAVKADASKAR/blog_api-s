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


