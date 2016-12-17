from django.db import models

# Create your models here.

class Container(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    container_id = models.CharField(max_length=100, blank=True, default='')
    container_name = models.CharField(max_length=100, blank=True, default='')
    container_image = models.CharField(max_length=100, blank=True, default='')
    container_status = models.CharField(max_length=100, blank=True, default='')
    container_ip = models.CharField(max_length=100, blank=True, default='')
    container_port = models.CharField(max_length=100, blank=True, default='')
    container_time = models.CharField(max_length=100, blank=True, default='')
    
