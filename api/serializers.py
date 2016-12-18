from rest_framework import serializers
from .models import Container

class ContainerSerializer(serializers.Serializer):
    image = serializers.CharField(max_length=100)
    #name = serializers.CharField(max_length=100)
    
    def create(self,validated_data):
    	return Container(**validated_data)

# class ListContainer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)


class ContainerListSerializer(serializers.ModelSerializer):

	class Meta:
		model = Container
		fields = (
					'id','created','container_id','container_name',
					'container_image','container_status'
				)