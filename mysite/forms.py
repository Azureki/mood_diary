#_*_ encoding: utf-8 *_*
from django import forms
from mysite import models
#Nick:Please add your data model here.

from captcha.fields import CaptchaField
from registration.forms import RegistrationForm
from django.contrib.auth.models import User

#Nick:Please design the extra user profile registration form.
#Nick:The extra user profile data will include height, gender, personal page url.



#Nick:Please design the login form.
class LoginForm(forms.Form):
    username = forms.CharField(label="username",max_length=20)
    password = forms.CharField(label='password',max_length=20,widget=forms.PasswordInput())
    captcha = CaptchaField(label="请输入图片中信息")

#Nick:Please design a date selection widget which might be a child class of forms.DateInput
from .models import Profile

class ProfileModel(forms.ModelForm):
    class Meta:  #定义Meta类，其中使用model注册数据模型
        model = Profile  #使用fields注册数据模型中的各个数据顷
        fields = [
            'height', 'gender', 'person_page','birthday'
            # 'user' # 加了这个似乎就可以改用户了
        ]

    def __init__(self, *args, **argv):  #调用父类构造凼数
        forms.ModelForm.__init__(self, *args, **argv)
        self.fields['height'].label = '身高:'
        self.fields['gender'].label = '性别:'
        self.fields['birthday'].label = '生日'
        self.fields['person_page'].label = '个人主页:'
        # self.fields['user'].label = '用户:'


from .models import Diary

class DiaryModel(forms.ModelForm):
    class Meta:  #定义Meta类，其中使用model注册数据模型
        model = Diary  #使用fields注册数据模型中的各个数据顷
        fields = [
            'budget', 'weight', 'note',
            # 'date',
            # 'user' # 加了这个似乎就可以改用户了
        ]

    def __init__(self, *args, **argv):  #调用父类构造凼数
        forms.ModelForm.__init__(self, *args, **argv)
        self.fields['budget'].label = '今日花费:'
        self.fields['weight'].label = '体重:'
        self.fields['note'].label = '日记:'
        # self.fields['date'].label = '日期'
#Nick:Please design the diary addition form, which should include budget, weight, note, date