from django.contrib import admin
from hotelapi.models import users,booking


# Register your models here.
# 第一種方式，未加入 ModelAdmin 類別 
admin.site.register(users)
admin.site.register(booking)
