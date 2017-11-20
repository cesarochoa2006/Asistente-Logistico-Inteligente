from django.conf.urls import url
from . import views

app_name = 'routes'
urlpatterns = [
    # /routes/
    url(r'^routes/$', views.IndexView.as_view(), name="index"),

]
