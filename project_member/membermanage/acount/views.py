from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import login, signup
from django.views.decorators.csrf import csrf_exempt
import datetime
import pymongo
from django.contrib.auth.models import User
from django.contrib import auth, messages



@csrf_exempt
def signupwork(request):
    # username = models.CharField(max_length=20)
    # identity = models.CharField(max_length=20)
    # password = models.CharField(max_length=20)
    # confirm_password = models.CharField(max_length=20)
    # user_email = models.CharField(max_length=40)
    if request.method == 'POST':
        username = request.POST['username']
        identity = request.POST['identity']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        useremail = request.POST['user_email']
        if confirm_password == password:
            print("\n*************password is same************\n")
            new_user = signup(username=username, identity=identity, password=password, user_email=useremail,
                              signup_date=datetime.datetime.now())
            new_user.save()
            return redirect('success/')
    # template.render(context, request) 를 넣어야하나?
    # return HttpResponse(request)
        else:  # 일단 패스워드가 틀리면 반려
            print('\n***********password is NOT same***********\n')

            template = loader.get_template('acount/signup.html')
            context = {
                'issuccess': 'you rejected any reason.2'
            }
            messages.error(request, "비밀번호가 다릅니다.")
            return HttpResponse(template.render(context, request))  # context 자리에 request를 넣으니 정보가 다운로드 되더라.
    template = loader.get_template('acount/signup.html')
    return HttpResponse(template.render({}, request))


def loginwork(request):
    template = loader.get_template('acount/login.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def logout(request):
    # TODO: 로그아웃 후 로그인 화면으로 돌아가기 구현
    pass


def Afterlogin(request):
    # TODO: 따로 앱으로 만들 것.
    pass

# Create your views here.
