# _*_ coding: utf-8 _*_
__auther__ = "tanran"
__date__ = "2017/3/19 19:59"

from .models import Course,Lesson,Video,CourseResource, BannerCourse
from organization.models import CourseOrg

import xadmin


class VideoInline(object):
    model = Video
    extra = 0

class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times','students','fav_nums','image','click_nums','add_time','get_zj_nums']
    search_fields = ['name', 'desc', 'detail', 'degree','students','fav_nums','image','click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times','students','fav_nums','image','click_nums','add_time']
    model_icon = 'fa fa-space-shuttle'
    readonly_fields = ['click_nums','fav_nums','students','is_banner']
    list_editable = ['name','degree','desc']
    style_fields = {"detail":"ueditor"}
    #列表刷新
    refresh_times = [5]

    def save_models(self):
        obj =  self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()



class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times','students','fav_nums','image','click_nums','add_time']
    search_fields = ['name', 'desc', 'detail', 'degree','students','fav_nums','image','click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times','students','fav_nums','image','click_nums','add_time']
    model_icon = 'fa fa-telegram'


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']
    model_icon = 'fa fa-tasks'
    inlines = [VideoInline]


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson__name', 'name', 'add_time']
    model_icon = 'fa fa-laptop'


class CourseResourceAdmin(object):
    list_display = ['course','name','download','add_time']
    search_field = ['course','name','download']
    list_filter = ['course','name','download','add_time']
    model_icon = 'fa fa-magic'


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(BannerCourse,BannerCourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)