from django.conf import settings 
import docker

client = docker.DockerClient(base_url='192.168.100.125:5555')


def create_container(image,detach=True):
	container = client.containers.run(image,detach=True)
	return container


def list_container(self):
	containers = client.containers.list()
	return containers

