from django.db import models
from block.models import Block

class Article(models.Model):
	block = models.ForeignKey(Block, verbose_name="所属版块", default=0)
	title = models.CharField("文章标题", max_length=100)
	content = models.CharField("文章内容", max_length=1000)
	status = models.IntegerField("状态", choices=((0,"正常"),(-1,"删除")), default=0)
	create_timestamp = models.DateTimeField("创建时间", auto_now_add=True)
	last_update_timestamp = models.DateTimeField("更新时间", auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "文章"
		verbose_name_plural = "数据表（文章）"
