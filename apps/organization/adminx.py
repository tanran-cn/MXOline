# _*_ coding: utf-8 _*_
__auther__ = "tanran"
__date__ = "2017/3/20 19:19"
import xadmin

from .models import CityDict,CourseOrg,Teacher

class CityDictAdmin(object):
    # name = models.CharField(max_length=20, verbose_name=u"城市")
    # desc = models.CharField(max_length=200, verbose_name=u"描述")
    # add_time = models.DateTimeField(default=datetime.now)
    list_display = ['name', 'desc', 'add_time']
    search_field = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']
    model_icon = 'fa fa-compass'


class CourseOrgAdmin(object):
    # name = models.CharField(max_length=50, verbose_name=u"机构名称")
    # desc = models.TextField(verbose_name=u"机构描述")
    # click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    # fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    # image = models.ImageField(upload_to="org/%Y/%m", verbose_name=u"封面图", max_length=100)
    # address = models.CharField(max_length=5, verbose_name=u"机构地址")
    # city = models.ForeignKey(CityDict, verbose_name=u"所在城市")
    # add_time = models.DateTimeField(default=datetime.now)
    list_display = ['name', 'desc', 'click_nums','fav_nums','image','address','city','add_time']
    search_field = ['name', 'desc', 'click_nums','fav_nums','image','address','city']
    list_filter = ['name', 'desc', 'click_nums','fav_nums','image','address','city','add_time']
    model_icon = 'fa fa-star'


class TeacherAdmin(object):
    # org = models.ForeignKey(CourseOrg, verbose_name=u"所属机构")
    # name = models.CharField(max_length=50, verbose_name=u"教师名称")
    # work_years = models.IntegerField(default=0, verbose_name=u"工作年限")
    # work_company = models.CharField(max_length=50, verbose_name=u"就职公司")
    # work_positon = models.CharField(max_length=50, verbose_name=u"公司职位")
    # points = models.CharField(max_length=50, verbose_name=u"教学特点")
    # click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    # fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    # add_time = models.DateTimeField(default=datetime.now)
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_positon', 'points', 'click_nums', 'fav_nums','add_time']
    search_field = ['org', 'name', 'work_years', 'work_company', 'work_positon', 'points', 'click_nums', 'fav_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_positon', 'points', 'click_nums', 'fav_nums','add_time']
    model_icon = 'fa fa-address-card'


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)