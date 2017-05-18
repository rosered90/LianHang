# -*- coding: utf-8 -*-
"""my323 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin
from django.views.static import  serve

from users.views import LoginView,RegisterView,AciveUserView,ForgetpwdView,ResetView,ModifyPwdView,LogoutView
from users.views import IndexView
from organization.views import OrgView
from my323.settings import MEDIA_ROOT,STATIC_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('^$',IndexView.as_view(),name="index"),
    url('^login/$', LoginView.as_view(), name="login"),

    url('^logout/$',LogoutView.as_view(),name="logout"),
    #（）是传方法的意思
    url('^register/$',RegisterView.as_view(),name="register"),
    url(r'^captcha/',include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$',AciveUserView.as_view(),name="user_active"),
    url(r'^forget/$',ForgetpwdView.as_view(),name="forget_pwd"),
    url(r'^reset/(?P<active_code>.*)/$',ResetView.as_view(),name="reset_pwd"),
    url(r'^modify_pwd/$',ModifyPwdView.as_view(),name="modify_pwd"),

    #课程机构URL配置
    url(r'^org/', include('organization.urls',namespace="org")),

    # 课程相关URL配置
    url(r'^course/', include('courses.urls', namespace="course")),

   #配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT}),

    # 配置上传文件的访问处理函数
    url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),
    # 课程相关URL配置
    url(r'^users/', include('users.urls', namespace="users")),



]

#全局404页面配置
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'