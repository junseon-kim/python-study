from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import login, signup
from django.views.decorators.csrf import csrf_exempt
import datetime
import pymongo

@csrf_exempt

def beforesign(request):

    template = loader.get_template('acount/signup.html')
    context = {}
    return render(request, 'acount/signup.html', context)

def signupwork(request):
    # username = models.CharField(max_length=20)
    # identity = models.CharField(max_length=20)
    # password = models.CharField(max_length=20)
    # confirm_password = models.CharField(max_length=20)
    # user_email = models.CharField(max_length=40)
    username = request.POST['username']
    identity = request.POST['identity']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']
    useremail = request.POST['user_email']
    new_user = signup(username=username, identity=identity, password=password, confirm_password=confirm_password,
                      user_email=useremail, signup_date=datetime.datetime.now())
    template = loader.get_template('acount/memberinfo.html')
    context = {
        'congataulation': 'WELCOME!'
    }
    new_user.save()

    return HttpResponse(template.render(context, request)) # context 자리에 request를 넣으니 정보가 다운로드 되더라.
    # template.render(context, request) 를 넣어야하나?
    # return HttpResponse(request)


def loginwork(request):
    # TODO: 로그인 구현
    pass


def logout(request):
    # TODO: 로그아웃 후 로그인 화면으로 돌아가기 구현
    pass


def Afterlogin(request):
    # TODO: 따로 앱으로 만들 것.
    pass

# Create your views here.
