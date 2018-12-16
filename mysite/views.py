# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib import auth

from forms import LoginForm, DiaryModel
from mysite.models import Diary
from .models import Profile
from django.contrib.auth.models import User
from django.utils import timezone
from forms import ProfileModel

# def index(request, pid=None, del_pass=None):
# from django.contrib.auth.decorators import login_required
# @login_required
def index(request):
    #As the home page, should check the authenticaiton status first,
    #if already login then use the username query the diaries data.
    #check the message instance, if any, show it.
    template = get_template('index.html')
    username = None


    if request.user.is_authenticated():
        messages.add_message(request,messages.SUCCESS,'%s的私人日记'% request.user.username)
        username = request.user.username
        user = User.objects.get(username=username)
        diaries=user.diary_set.all()

    else:
        messages.add_message(request,messages.WARNING,'请先登录')
    html = template.render(locals(),request)
    return HttpResponse(html)

#user function decorator login_required to check whether or not it already login, if not, redirect to login page
def userinfo(request):
    #should check the authenticaiton status first,
    #if already login then use the username query the profile data.
    #if the form submit, check the validity of form data, if valid, save data and show success information.
    #if not, show error message.Please use the message mechanism.
    #if current access is the first time show page, then display the userinfo form.
    username = request.user.username
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    else:
        template = get_template('userinfo.html')
        user = User.objects.get(username=username)
        instance = Profile.objects.get(user=user)

        Profiles = ProfileModel(instance=instance)

        if request.method == 'GET':
            html = template.render(locals(), request)
        else:
            Profiles = ProfileModel(request.POST, instance=instance)
            if Profiles.is_valid():
                messages.add_message(request, messages.SUCCESS, '保存成功')
                Profiles.save()
            else:
                messages.add_message(request, messages.WARNING, '保存失败')
            html = template.render(locals(), request)
        return HttpResponse(html)


def login(request):
    #should check the authenticaiton status first,if already login, redirect to home page.
    #if the form submit, check the validity of form data, if valid, use the username and password to perform
    # authentication. if the user is not valid or not been activated, then display the respective message.
    #if the user is valid, then login and display the success message.
    #if current access is the first time show page, then display the login form.
    template = get_template('login.html')
    username = None


    if request.user.is_authenticated():
        messages.add_message(request,messages.INFO,'Welcome %s'% request.user.username)
        username = request.user.username
    else:
        if request.method == 'GET':
            loginform = LoginForm()
        else:
            loginform = LoginForm(request.POST)
            if loginform.is_valid():
                username = auth.authenticate(request,\
                                             username = loginform.cleaned_data['username'],\
                                             password = loginform.cleaned_data['password'],\
                                             )
                if username and username.is_active:
                    messages.add_message(request,messages.INFO,'Welcome %s !'% username)
                    auth.login(request,username)
                else:
                    username = None
                    messages.add_message(request,messages.WARNING,'Please check your login id/password')
            else:
                username = None
                messages.add_message(request,messages.WARNING,'Please check your login id/password')
    html = template.render(locals(),request)
    return HttpResponse(html)



def logout(request):
    #logout current user.
    #Display the logout message.
    #redirect to home page.
    auth.logout(request)
    messages.add_message(request,messages.SUCCESS,'你已成功注销')
    return HttpResponseRedirect('/home')


#user function decorator login_required to check whether or not it already login, if not, redirect to login page
def posting(request):
    #should check the authenticaiton status first,if already login, get the username.
    #should display the message contents if any.
    # if the form submit, check the validity of form data, if valid, save the diary data and show success message.
    #Tips: should user the instance key parameter which specify the diary data model instance otherwise you cannot
    #save data.
    #if current access is the first time show page, then display the login form, and show a reminder message.
    username = None
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    else:
        username = request.user.username
        user = User.objects.get(username=username)
        # instance=Diary.objects.get(id=1)

        template = get_template('posting.html')
        if request.method == 'GET':

            new_diary = DiaryModel()
            html = template.render(locals(), request)
        else:
            instance = Diary(user=user, date=timezone.now().date())
            new_diary = DiaryModel(request.POST, instance=instance)
            if new_diary.is_valid():
                messages.add_message(request,messages.SUCCESS,'保存成功')


                #errormsg = '保存成功'
                new_diary.save()
            else:
                messages.add_message(request,messages.WARNING,'保存失败')
                #errormsg = '保存失败'
            html = template.render(locals(), request)
        return HttpResponse(html)

