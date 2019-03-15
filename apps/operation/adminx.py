# _*_ coding: utf-8 _*_
__auther__ = "tanran"
__date__ = "2017/3/20 19:29"
import xadmin

from .models import UserAsk,CourseComents,UserFavorite,UserMessage,UserCourse

class UserAskAdmin(object):
    # name = models.CharField(max_length=20, verbose_name=u"姓名")
    # mobile = models.CharField(max_length=11, verbose_name=u"手机")
    # course_name = models.CharField(max_length=50, verbose_name=u"课程名")
    # add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_field = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']
    model_icon = 'fa fa-tty'


class CourseComentsAdmin(object):
    # user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    # course = models.ForeignKey(Course, verbose_name=u"课程")
    # coments = models.CharField(max_length=200, verbose_name=u"评论")
    # add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    list_display = ['user', 'course', 'coments', 'add_time']
    search_field = ['user', 'course', 'coments']
    list_filter = ['user', 'course', 'coments', 'add_time']
    model_icon = 'fa fa-pencil-square'


class UserFavoriteAdmin(object):
    # user = models.ForeignKey(UserProfile, verbose_name="用户")
    # fav_id = models.IntegerField(default=0, verbose_name="数据ID")
    # fav_type = models.IntegerField(choices=((1, "课程"), (2, "课程机构"), (3, "讲师")), default=1, verbose_name=u"收藏类型")
    # add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_field = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']
    model_icon = 'fa fa-thumbs-up'


class UserMessageAdmin(object):
    # user = models.IntegerField(default=0, verbose_name=u"接受用户")
    # message = models.CharField(max_length=200, verbose_name=u"消息内容")
    # has_read = models.BooleanField(default=False, verbose_name=u"是否已读")
    # add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_field = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']
    model_icon = 'fa fa-volume-control-phone'


class UserCourseAdmin(object):
    # user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    # course = models.ForeignKey(Course, verbose_name=u"课程")
    # add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    list_display = ['user', 'course', 'add_time']
    search_field = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']
    model_icon = 'fa fa-tags'


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComents, CourseComentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)


