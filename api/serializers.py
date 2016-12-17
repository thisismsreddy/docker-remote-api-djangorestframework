from rest_framework import serializers

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

