from django.contrib import admin
#Nick:Please add your data model here.

#Nick:Please create a admin display configuration class here.

#Nick:Please register your data models

from models import Profile



admin.site.register(Profile)

from models import Diary
class DiaryAdmin(admin.ModelAdmin):
    list_display=('user','budget','weight','date')
    search_fields=('budget','weight','note')
    ordering=('-date',)
admin.site.register(Diary,DiaryAdmin)