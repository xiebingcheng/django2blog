from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    # 文章分类

    name = models.CharField(verbose_name="文章类别", max_length=20)

    class Meta:
        verbose_name = '文章类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    # 文章标签

    name = models.CharField(verbose_name='文章标签', max_length=20)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Blog(models.Model):
    # 博客表

    title = models.CharField(verbose_name='标题',max_length=100)
    content = models.TextField(verbose_name='正文',default='')
    create_time = models.DateTimeField(verbose_name='创建时间',default=timezone.now)
    modify_name = models.DateTimeField(verbose_name="修改时间",auto_now=True)
    click_nums = models.IntegerField(verbose_name='点击量',default=0)
    # 一个文章类别可以对应多个博客文章,但是一篇文章类别只能有一个分类,所以文章分类包含博客
    # django2.0新增 on_delete 参数
    category = models.ForeignKey(Category, verbose_name='文章类别',on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='文章标签')

    class Meta:
        verbose_name = '我的博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
