from djongo import models
from app.utils import get_upload_file_dir_path
import datetime


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    user_create_time = models.DateTimeField()
    token = models.CharField(max_length=100)
    token_expire_time = models.DateTimeField()
    vip = models.BooleanField()
    vip_create_time = models.DateTimeField()
    vip_expire_time = models.DateTimeField()


def path_and_rename(instance, filename):
    overdate = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    # ['filename', 'suffix']
    fname = filename.split('.')
    newname = overdate + '_' + fname[0] + '.' + fname[1]
    return get_upload_file_dir_path(newname)


class FileInfo(models.Model):
    share_code = models.CharField(max_length=100, unique=True)
    file_size = models.IntegerField()
    file_name = models.CharField(max_length=100)
    download_count = models.IntegerField()
    create_user = models.CharField(max_length=100)
    file_expire_time = models.DateTimeField()
    file = models.FileField(upload_to=path_and_rename)

