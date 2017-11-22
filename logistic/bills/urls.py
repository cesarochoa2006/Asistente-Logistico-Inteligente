from django.conf.urls import url
from . import views

app_name = 'bills'
urlpatterns = [
    # /bills/
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^upload_file/$', views.UploadFile.as_view(), name="upload_file"),
    url(r'^delete_file/(?P<pk>[0-9]+)$', views.FileDelete.as_view(), name='delete_file'),
    url(r'^update_file/(?P<pk>[0-9]+)$', views.UpdateFile.as_view(), name='update_file'),


]
