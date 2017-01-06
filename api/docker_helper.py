from django.conf import settings
import json 
import docker

client = docker.DockerClient(base_url='192.168.100.125:5555')


def create_container(image,detach=True):
	container = client.containers.run(image,detach=True)
	return container


def list_container():
	emt_dict=[]
	containers = client.containers.list()
	for i in containers:
		whaterver=(json.dumps({'ID':str(i.id[0:12]),'Name':str(i.name),'Created':str(i.attrs['Created'])}))
		emt_dict.append(whaterver)
	return emt_dict 