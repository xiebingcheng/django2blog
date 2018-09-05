from django.shortcuts import render
from django.views import View

from blog.models import Blog, Category, Tag
# Create your views here.


class IndexView(View):
    # 首页后端函数

    def get(self,request):
        # 获取数据库中的数据渲染到index页面上
        all_blog = Blog.objects.all().order_by('-id')
        return render(request,'index.html', {
            'all_blog': all_blog
        })