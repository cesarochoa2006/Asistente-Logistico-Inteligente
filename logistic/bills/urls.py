from django.conf.urls import url
from . import views

app_name = 'bills'
urlpatterns = [
    # /bills/
    url(r'^$', views.IndexView.as_view(), name="index"),

]
