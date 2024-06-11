from home.models import *
from rest_framework import serializers

class blogserializer(serializers.ModelSerializer):

    class Meta:
        model=blog
        fields="__all__"
        

