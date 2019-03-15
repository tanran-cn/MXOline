# _*_ coding: utf-8 _*_
__auther__ = "tanran"
__date__ = "2017/3/18 23:43"

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row

from .models import EmailVerifyRecord,Banner, UserProfile


class UserProfileAdmiin(UserAdmin):
   pass


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobaSettings(object):
    site_title = "慕学后台管理系统"
    site_footer = "慕学在线网"
    menu_style = "accordion"


class BannerAmin(object):
    list_display = ['title', 'image', 'url', 'index','add_time']
    search_fields = ['title', 'image','url','index']
    list_filter = ['title', 'image', 'url', 'index','add_time']
    model_icon = 'fa fa-television'

class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type']
    list_filter = ['code','email','send_type','send_time']
    model_icon = 'fa fa-address-book-o'

# from  django.contrib.auth.models import User
# xadmin.site.unregister(User)
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAmin)
# xadmin.site.register(UserProfile,UserProfileAdmiin)

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobaSettings)