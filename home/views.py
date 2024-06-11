from django.shortcuts import render
from home.serializer import *
from rest_framework.decorators import api_view,APIView
from rest_framework.authtoken.models import Token
from home.models import *
from rest_framework.response import Response

# creating a user

class create_user(APIView):
    def post(self,request):
        serializer=Userserializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':200,'message':serializer.errors})
        serializer.save()
        user=User.objects.get(username=serializer.data['username'])
        token , _ = Token.objects.get_or_create(user=user)
        return Response({'message':'User is created successfully','token':str(token)})
    
    

# for list of Blog's
class getblog(APIView):
    def get(self,request):
        obj_1=blog.objects.all()
        serializer=blogserializer(obj_1,many=True)
        return Response({'status':200,'data':serializer.data})
    
# for deleting the Blog's
class delete_blog(APIView):
    def delete(self,request,id):
        obj_2=blog.objects.filter(id=id)
        if obj_2.exists():
            obj_2.delete()
            data={'message':'blog deleted successfully'}
            return Response(data)
        return Response({'Blog does not exists'})
# for creating a Blog
class create_blog(APIView):
    def POST(self,request):
        serializer=blogserializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':200,'message':serializer.errors})
        serializer.save()
        return Response({'status':200,'message':'Blog is created successfully'})

# for updating a Blog
class update_blog(APIView):
    def put(self,request,id):
        obj_3=blog.objects.get(id=id)
        serializer=blogserializer(obj_3,data=request.data)
        if not serializer.is_valid():
            return Response({'status':200,'message':serializer.errors})
        serializer.save()
        return Response({'status':200,'message':'Blog  is updated successfully'})
