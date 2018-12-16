# _*_ encoding: utf-8 _*_
from django.db import models
from django.contrib.auth.models import User

#Nick:Please design the extra user profile data model which should be a extension of
#Django standard user profile, the extra data should include height, gender, personal page url.

#Nick:Please design the data model which save the diary information. It should include the budget,
#weight, note, date.
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    male='male'
    female='female'

    gender_select=(
        (male,'男'),
        (female,'女')
    )
    # nickname=models.CharField(max_length=50,blank=True)
    height=models.FloatField(null=True)
    gender=models.CharField(null=True,max_length=20,choices=gender_select,default=male)
    person_page=models.URLField(null=True)
    birthday = models.DateField(null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Diary(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户名')
    budget=models.FloatField(null=True,verbose_name='预算')
    weight=models.FloatField(null=True,verbose_name='体重')
    note=models.TextField(null=True,verbose_name='笔记')
    date = models.DateField(null=True,verbose_name='日期')