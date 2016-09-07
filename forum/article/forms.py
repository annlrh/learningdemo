from django import forms
from .models import Article

'''

class ArticleForm(forms.Form):
	title = forms.CharField(label="标题", max_length=100, required=True)
	content = forms.CharField(label="内容", max_length=10000, required=True)
'''

#更简单的校验，利用models数据表结构完成对表单数据的校验
class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ["title", "content"]

