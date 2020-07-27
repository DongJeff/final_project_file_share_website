from django.test import TestCase
from app.utils import *
import os
import datetime

if __name__ == '__main__':
    # for i in range(1, 10):
    #     # print(generate_share_code())
    #     print(generate_token())
    # print(get_upload_file_dir_path())
    now = datetime.datetime.utcnow()
    print(get_current_time())
