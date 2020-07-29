from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from app.serializers import *
from django.shortcuts import render
import datetime
import app.utils as utils


class IndexView(APIView):
    def get(self, request):
        return render(request, 'index.html')


class LoginView(APIView):
    def post(self, request):
        ser = LoginFormSerializer(data=request.data)
        if not ser.is_valid():
            return JsonResponse({'code': 400, 'msg': ser.errors})
        try:
            user = User.objects.get(username=ser.data['username'])
        except User.DoesNotExist:
            return JsonResponse({'code': 401, 'msg': 'username or password error'})
        if user.password == ser.data['password']:
            now = utils.get_current_time()
            user.token = utils.generate_token()
            user.token_expire_time = now + datetime.timedelta(days=10)
            user.save()
            return JsonResponse({'code': 200, 'msg': "success", 'data': UserSerializer(user).data})
        return JsonResponse({'code': 401, 'msg': 'username or password error'})


class RegisterView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            user = User()
            user.username = username
            user.password = password
            user.user_create_time = utils.get_current_time()
            user.save()
            return JsonResponse({'code': 200, 'msg': "success"})

        return JsonResponse({'code': 400, 'msg': "username has exist"})


class FileView(APIView):
    # parser_classes = (FileUploadParser,)

    def get(self, request):
        try:
            user = get_user(request)
        except Exception as e:
            return JsonResponse({'code': 401, 'msg': e.args[0]})
        share_code = request.query_params['share_code']
        try:
            file_info = FileInfo.objects.get(share_code=share_code)
        except FileInfo.DoesNotExist:
            return JsonResponse({'code': 400, 'msg': "file not exist"})
        if utils.is_expired(file_info.file_expire_time):
            return JsonResponse({'code': 400, 'msg': "the file has expired"})

        file_path = str(file_info.file)
        with open(file_path, 'rb') as f:
            file = f.read()
        response = HttpResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        file_name = file_info.file_name
        response['Content-Disposition'] = 'attachment;filename=%s' % file_name
        file_info.download_count += 1
        file_info.save()
        return response

    def post(self, request, *args, **kwargs):
        try:
            user = get_user(request)
        except Exception as e:
            return JsonResponse({'code': 401, 'msg': e.args[0]})

        file = request.data['file']

        file_info = FileInfo()
        file_info.share_code = utils.generate_share_code()
        file_info.file_name = file.name
        file_info.create_user = user.username
        file_info.download_count = 0
        file_info.file_size = file.size
        # If the user is not vip, the upload file size will be limited to 10MB
        if not vip_validate(user):
            if file.size / 1024 / 1024 > 10:
                return JsonResponse(
                    {'code': 400,
                     'msg': "File size cannot be larger than 10MB, if you want to upload larger file, be a VIP !"})
        file_info.file = file
        # If the user is vip, he/she can keep the file more than 1 day
        file_keep_day = 1
        if vip_validate(user):
            file_keep_day = 30
        file_info.file_expire_time = utils.get_current_time() + datetime.timedelta(days=file_keep_day)
        file_info.save()

        return JsonResponse({'code': 200, 'msg': "success", 'share_code': file_info.share_code})


def vip_validate(user: User):
    if user.vip is None:
        user.vip = False
        user.save()
        return False
    if not user.vip:
        return False
    return not utils.is_expired(user.vip_expire_time)


def get_user(request):
    try:
        token = request.META['HTTP_TOKEN']
    except Exception as e:
        raise Exception("Please put token in headers")
    try:
        user = User.objects.get(token=token)
        if utils.is_expired(user.token_expire_time):
            raise Exception("token is expired")
        return user
    except User.DoesNotExist:
        raise Exception("token not available")


class TestView(APIView):
    def get(self, request):
        try:
            user = get_user(request)
        except Exception as e:
            return JsonResponse({'code': 401, 'msg': e.args[0]})
        return JsonResponse({'code': 200, 'msg': "success"})


class VipView(APIView):
    # Check the user is vip or not
    def get(self, request):
        try:
            user = get_user(request)
        except Exception as e:
            return JsonResponse({'code': 401, 'msg': e.args[0]})
        return JsonResponse({'code': 200, 'msg': "success", 'is_vip': vip_validate(user)})

    # simply simulate the user to top up
    def post(self, request):
        try:
            user = get_user(request)
        except Exception as e:
            return JsonResponse({'code': 401, 'msg': e.args[0]})
        charge = int(request.data['charge'])

        if charge < 10:
            return JsonResponse({'code': 440, 'msg': "it's not enough"})
        user.vip = True
        user.vip_create_time = utils.get_current_time()
        user.vip_expire_time = user.vip_create_time + datetime.timedelta(days=30)
        user.save()
        return JsonResponse({'code': 200, 'msg': "success! you are vip now!"})

