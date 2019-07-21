#-*-coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django import forms

class News(models.Model):
    title=models.CharField(max_length=20)
    content=models.CharField(max_length=1000)



KIND_CHOICES=(
('技术','技术'),
('新闻','新闻'),
('财务','财务'),
('人力','人力'),
('公关','公关'),
('团队','团队'),
)
class Moment(models.Model):
    xiaoxi=models.CharField('请输入您想要说的内容',max_length=200)
    user_name=models.CharField('请输入您的名字',max_length=20,default='匿名')
    kind=models.CharField('请选择您要留言的对象',max_length=20,choices=KIND_CHOICES,default=KIND_CHOICES[0])
    def __str__(self):
        return self.user_name


# Create your models here.
