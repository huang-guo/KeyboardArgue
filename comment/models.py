from django.db import models
from battle.models import Battle


# Create your models here.
class Comment(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    content = models.TextField(verbose_name="内容")
    target = models.ForeignKey(
        Battle,
        on_delete=models.CASCADE,
        verbose_name="评论目标"
    )
    side = models.PositiveSmallIntegerField(
        choices=((1, 'red'), (2, 'blue')),
        verbose_name="站边"
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="创建时间"
    )

    def __str__(self):
        if len(self.content) >= 10:
            return self.content[:10]+"..."
        else:
            return self.content

    class Meta:
        verbose_name = verbose_name_plural = "观点"
