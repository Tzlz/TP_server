import json

from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import User, Temp


@csrf_exempt
def login(request):
    dic = {}
    if request.method == 'GET':
        dic['status'] = "Failed"
        dic['message'] = "Wrong Method"
        return HttpResponse(json.dumps(dic))
    try:
        post_content = json.loads(request.body)
        username = post_content['username']
        password = post_content['password']
        user = User.objects.get(username=username)
    except (KeyError, json.decoder.JSONDecodeError):
        dic['status'] = "Failed"
        dic['message'] = "No Input"
        return HttpResponse(json.dumps(dic))
    except User.DoesNotExist:
        dic['status'] = "Failed"
        dic['message'] = "Wrong Username"
        return HttpResponse(json.dumps(dic))
    if check_password(password, user.password):

        dic['status'] = "Success"
        # dic['user_id'] = user.id
        # dic['photo_url'] = user.photo_url
        return HttpResponse(json.dumps(dic))
    else:
        dic['message'] = "Wrong Password"
        dic['status'] = "Failed"
        return HttpResponse(json.dumps(dic))


@csrf_exempt
def register(request):
    dic = {}
    if request.method == 'GET':
        dic['status'] = "Failed"
        dic['message'] = "Wrong Method"
        return HttpResponse(json.dumps(dic))
    try:
        post_content = json.loads(request.body)
        username = post_content['username']
        password = post_content['password']
        user = User.objects.get(username=username)
    except (KeyError, json.decoder.JSONDecodeError):
        dic['status'] = "Failed"
        dic['message'] = "No Input"
        return HttpResponse(json.dumps(dic))
    except User.DoesNotExist:
        dic['status'] = "Success"
        encry_password = make_password(password)
        newUser = User(username=username, password=encry_password)
        newUser.save()
        return HttpResponse(json.dumps(dic))
    if user is not None:
        dic['status'] = "Failed"
        dic['message'] = "User exist"
        return HttpResponse(json.dumps(dic))


@csrf_exempt
def get_temp(request):
    dic = {}
    if request.method == 'GET':
        dic['status'] = "Failed"
        dic['message'] == "Wrong Method"
        return HttpResponse(json.dumps(dic))
    try:
        post_content = json.loads(request.body)
        date = post_content['date']
        temp = Temp.objects.get(date=date)
    except (KeyError, json.decoder.JSONDecodeError):
        dic['status'] = "Failed"
        dic['message'] = "No Input"
        return HttpResponse(json.dumps(dic))
    # except temp.DoesNotExist:
    #     dic['status'] = "Success"
    #     return HttpResponse(json.dumps(dic))
    # if temp is not None:
    #     dic['status'] = "Failed"
    #     dic['message'] = "User exist"
    #     return HttpResponse(json.dumps(dic))


# Create your views here.
