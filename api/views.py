from rest_framework.response import Response 
from rest_framework.views import APIView
from .serializers import ContainerSerializer, ContainerListSerializer
from rest_framework import status,views,generics
from django.shortcuts import render
from docker_helper import create_container,list_container
from .models import Container
from rest_framework import generics


class CreateContainerView(generics.CreateAPIView):
    """
    This api endpoint take two inputs and return result
    """
    serializer_class = ContainerSerializer
    def post(self, request, format=None):
        serializer = ContainerSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.validated_data.get('image')
            
            #name = serializer.validated_data.get('name')
            conainer = create_container(image)
            ct = Container.objects.create(
                        container_id= conainer.id,
                        container_name = conainer.name,
                        container_image = image,
                        container_status = conainer.status

                )
            ct.save()

            s = serializer.data
            # here we can perform any third party api calls and get the result and inject into dict
            s.update({'Name' : conainer.name, 'status': conainer.status,'Id':conainer.id[0:8]})
            return Response(s,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContainerList(APIView):

    def get(self,request,*args,**kw):
        result = list_container()
        response = Response(result,status=status.HTTP_200_OK)
        return response


# class ContainerList(generics.ListCreateAPIView):
#     queryset = Container.objects.all()
#     serializer_class = ContainerListSerializer


class ContainerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Container.objects.all()
    serializer_class = ContainerListSerializer