#blog/adminx.py
#xadmin的设置文件

import xadmin
from .models import Category, Tag, Blog


# 注册xadmin的功能,完善表结构

#在xadmin注册文章分类
class CategoryAdmin(object):
    # 显示的列表
    list_display = ['name']
    # 搜索的字段,不能添加时间,容易出错
    search_fields = ['name']
    # 过滤
    list_filter = ['name']

xadmin.site.register(Category,CategoryAdmin)


#注册标签
class TagAdmin(object):
    # 显示的列表
    list_display = ['name']
    # 搜索的字段,不能添加时间,容易出错
    search_fields = ['name']
    # 过滤
    list_filter = ['name']

xadmin.site.register(Tag,TagAdmin)


#注册博客
class BlogAdmin(object):
    # 显示的列表
    list_display = ['title','content','create_time','modify_name','click_nums','category','tag']
    # 搜索的字段,不能添加时间,容易出错
    search_fields = ['title','content','modify_name','click_nums','category','tag']
    # 过滤
    list_filter = ['title','content','create_time','modify_name','click_nums','category','tag']


xadmin.site.register(Blog,BlogAdmin)