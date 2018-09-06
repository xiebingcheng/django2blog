from django.shortcuts import render
from django.views import View

from pure_pagination import PageNotAnInteger, Paginator

from blog.models import Blog, Category, Tag
# Create your views here.


class IndexView(View):
    # 首页后端函数

    def get(self,request):
        # 获取数据库中的数据渲染到index页面上
        all_blog = Blog.objects.all().order_by('-id')

        # 首页的分页逻辑
        try:
            page = request.GET.get('page',1)
        except PageNotAnInteger:
            page = 1
        #     设置每页展示博客的数目
        p = Paginator(all_blog, 5, request=request)
        all_blog = p.page(page)

        return render(request,'index.html', {
            'all_blog': all_blog,
        })


class ArichiveView(View):

    def get(self, request):
        all_blog = Blog.objects.all().order_by('-create_time')

        # 分页
        try:
            page = request.GET.get('page',1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_blog,5,request=request)
        all_blog = p.page(page)

        return render(request, 'archive.html', {
            'all_blog' : all_blog,
        })