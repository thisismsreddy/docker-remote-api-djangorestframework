from django.conf import settings
import json 
import docker

client = docker.DockerClient(base_url='192.168.130.123:5555')


def create_container(image,detach=True):
	container = client.containers.run(image,detach=True)
	return container


# i.attrs['Config']['Image']
# i.attrs['Config']['ExposedPorts']
# i.attrs['NetworkSettings']['IPAddress']
# i.status


def list_container():
	emt_dict=[]
	containers = client.containers.list()
	for i in containers:
		whaterver=({'ID':str(i.id[0:10]),'Name':str(i.name), 
					'Status':str(i.status),'Created':str(i.attrs['Created']),
					'IPAddress':str(i.attrs['NetworkSettings']['IPAddress']),
					'Service':str(i.attrs['Config']['Image']),
					'Ports':str(i.attrs['Config']['ExposedPorts'])})
		emt_dict.append(whaterver)
	return emt_dict 