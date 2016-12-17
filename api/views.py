from rest_framework.response import Response 
from .serializers import ContainerSerializer
from rest_framework import status,views,generics
from django.shortcuts import render
from docker_helper import create_container,list_container




# class DistanceView(views.APIView):
#     """
#     This api endpoint take two inputs and return result
#     """
    
#     def post(self, request, format=None):
#         serializer = DistanceSerializer(data=request.data)
#         if serializer.is_valid():
#             subject = serializer.validated_data.get('city1')
#             # In this example we can take extra argumnet make it optnal
#             #useing the .get method in python dic
#             # exp we need to add some other city between this two citys 
#             # in that case we can likethis
#             # validate_data.get('city3', None)
            
#             message = serializer.validated_data.get('city2')
#             #do something with data and return the data like dist(city1-city2)
#             s = serializer.data
#             # here we can perform any third party api calls and get the result and inject into dict
#             s.update({'distacne': subject+message})
#             return Response(s,status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

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
            s = serializer.data
            # here we can perform any third party api calls and get the result and inject into dict
            s.update({'Name' : conainer.name, 'status': conainer.status,'Id':conainer.id[0:8]})
            return Response(s,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)