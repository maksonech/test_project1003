import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .mig.models import init_user


def index(request):
    return HttpResponse("Test message")


def login(request):
    return render(request, 'login.html', {'msg': 'Логинка'})


def added_user(request):
    en = init_user(username=request.POST.get('name'), password=request.POST.get('password'))
    en.save()
    str1 = "Data inserted to auth_user table"
    return render(request, 'login.html', {'msg': str1})


def viev_messages(request):
    return HttpResponse("Типо выводим сообщения")


@csrf_exempt
def results(request):
    data = json.loads(request.body.decode())
    name = data['name']
    message = data['message']
    responce = name, ' ', message
    return HttpResponse(responce)
