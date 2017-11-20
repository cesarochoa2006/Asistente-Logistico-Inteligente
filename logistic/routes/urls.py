from django.conf.urls import url
from . import views

app_name = 'routes'
urlpatterns = [
    # /routes/
    url(r'^$', views.IndexView.as_view(), name="index"),

]
