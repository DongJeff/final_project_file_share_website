import uuid
import os
import datetime
import pytz


def generate_token():
    # uuid4 is create by random
    return str(uuid.uuid4())


def generate_share_code():
    return str(uuid.uuid4()).split('-')[0][0:5]


def get_upload_file_dir_path(file_name=''):
    absp = os.path.abspath('.')
    dir_path = os.path.join(absp, "upload")
    return os.path.join(dir_path, file_name)


def get_current_time():
    """
    The mongodb and djongo will store isodate in mondodb, so we should also use iso time in python
    :return:
    """
    utc_tz = pytz.timezone('UTC')
    return datetime.datetime.now(tz=utc_tz)


def is_expired(time):
    """
    :param time: datetime.datetime() with timezone
    :return:
    """
    return time.__lt__(get_current_time())
