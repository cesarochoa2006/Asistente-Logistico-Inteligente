from django.db import models
from django.db import models
from jsonfield import JSONField
from collections import OrderedDict


# Create your models here.
#Manage Excel Files
class File(models.Model):
    file_file = models.FileField(default='')
    thumbnail = models.CharField(max_length=250, default='https://www.mathworks.com/matlabcentral/mlc-downloads/downloads/submissions/48551/versions/6/screenshot.jpg')
#Store and retrieve Json Data
class Data(models.Model):
    json= JSONField(load_kwargs={'object_pairs_hook': OrderedDict})

