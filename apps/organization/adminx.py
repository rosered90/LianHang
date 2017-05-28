# coding:utf-8
__author__ = 'fang'
__date__ = '2017/3/23 0023 14:28'


import xadmin
from .models import CityDict,CourseOrg,Teacher

class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = [ 'name', 'desc','click_num','fav_num','image','address','city','add_time']
    search_fields = [ 'name', 'desc','click_num','fav_num','image','address','city']
    list_filter = [ 'name', 'desc','click_num','fav_num','image','address','city','add_time']
    # relfield_style = 'fk-ajax'


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'points','click_num','fav_num','add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'points','click_num','fav_num','add_time']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'points','click_num','fav_num','add_time']

xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register( Teacher, TeacherAdmin)
