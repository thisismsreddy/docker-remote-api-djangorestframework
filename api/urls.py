from django.conf.urls import include, url
from .views import CreateContainerView , ContainerList , ContainerDetail

urlpatterns = [
    url(r'^$', CreateContainerView.as_view(), name='container'),
    url(r'^list/$', ContainerList.as_view(), name='container_detail'),
    url(r'^container_detail/(?P<pk>[0-9]+)/$', ContainerDetail.as_view(), name='container_detail'),

]