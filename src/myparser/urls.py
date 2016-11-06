from django.conf.urls import url

from .views import UploadFile

urlpatterns = [
    url(r'^$', UploadFile.as_view(), name='base'),
]
