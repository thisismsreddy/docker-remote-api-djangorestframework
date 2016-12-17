from django.conf.urls import include, url
from .views import CreateContainerView

urlpatterns = [
    url(r'^$', CreateContainerView.as_view(), name='container')
]