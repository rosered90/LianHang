# coding:utf-8
__author__ = 'fang'
__date__ = '2017/4/6 0006 16:34'

import re
from django import forms

from operation.models import UserAsk



class USerAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        """
        验证手机号码是否合法,必须以clean开头
        clean是对每一个字段进行自定义封装
        """
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"


        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法", code="mobile_invalid")
