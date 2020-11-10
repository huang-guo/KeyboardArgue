from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DEACTIVATE = 2
    STATUS = [
        (STATUS_NORMAL, "正常"),
        (STATUS_DEACTIVATE, "停用")
    ]
    status = models.PositiveSmallIntegerField(choices=STATUS,
                                              default=STATUS_NORMAL,
                                              verbose_name="状态"
                                              )
    name = models.CharField(max_length=50, verbose_name="分类")
    creator = models.ForeignKey(User, models.SET_NULL,
                                blank=True, null=True,
                                verbose_name="创建者"
                                )
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "分类"


class Battle(models.Model):
    STATUS_REVIEWED = 1
    STATUS_NORMAL = 2

    STATUS_DELETE = 3
    STATUS = [
        (STATUS_REVIEWED, "审核"),
        (STATUS_NORMAL, "正常"),
        (STATUS_DELETE, "删除")
    ]
    status = models.PositiveSmallIntegerField(choices=STATUS, default=STATUS_REVIEWED)
    theme = models.CharField(max_length=200, verbose_name="主题")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="分类")
    creator = models.ForeignKey(User, models.SET_NULL,
                                blank=True, null=True,
                                verbose_name="创建者"
                                )
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    red_name = models.CharField(max_length=200, verbose_name="红方辩题")
    blue_name = models.CharField(max_length=200, verbose_name="蓝方辩题")
    watch_number = models.IntegerField(default=0, verbose_name="围观人数")

    def get_red_count(self):
        pass

    def get_blue_count(self):
        pass

    class Meta:
        verbose_name = verbose_name_plural = "对战"
