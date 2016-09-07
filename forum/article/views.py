from django.shortcuts import render, redirect

from block.models import Block
from .models import Article

from .forms import ArticleForm

from django.views.generic import View

from utils.paginator import paginate_queryset

#from django.http import HttpResponse

def article_list(request, block_id):	

	#block_id，参数传递时字符串类型，int转换成整数类型
	block_id = int(block_id)
	#获取Block数据表数据
	block = Block.objects.get(id=block_id)

	'''
	#计算一页的开始索引和结束索引
	start_index = (page_no-1)*Article_CNT_1Page
	end_index = page_no*Article_CNT_1Page

	#获取Article数据表数据，筛选模块id=block_id，状态为0的文章，并分页
	articles_objs = Article.objects.filter(block=block, status=0).order_by("-id")[start_index:end_index]
	'''

	page_no = int(request.GET.get("page_no","1"))
	
	#获取Article数据表全部数据
	all_articles = Article.objects.filter(block=block, status=0).order_by("-id")

	#调用/utils/paginator.py中的函数paginate_queryset
	articles_objs, pagination_data = paginate_queryset(all_articles, page_no)

	#返回article_list.html页面，并传递参数
	return render(request, "article_list.html", {"articles": articles_objs, "pagination_data": pagination_data})


'''
#基于函数的写法

def Article_Create(request, block_id):

	#block_id，参数传递为字符串类型，需要int转换成整型
	block_id = int(block_id)
	#获取Block数据表模块数据
	block = Block.objects.get(id=block_id)
		
	if request.method == "GET":
		#请求表单页面
		return render(request, "article_create.html", {"b":block})
	else:
		#表单提交
		title = request.POST["inputTitle"].strip()
		content = request.POST["inputContent"].strip()
		
		#判断标题和内容是否为空
		if not title or not content:
			return render(request, "article_create.html", {"b": block, "error": "标题和内容都不能为空！", "title": title, "content": content})

		#判断标题长度不长于100，内容长度不长于10000
		if len(title) > 100 or len(content) > 10000:
			return render(request, "article_create.html", {"b": block, "error": "标题或内容超出长度！", "title": title, "content": content})

		#表单数据存入数据表
		article = Article(block=block, title=title, content=content, status=0)
		article.save()
		#数据存入数据表后，页面重定向到文章列表页面
		return redirect("/article/list/%s" % block_id)
'''

#基于类的写法，继承View类
class Article_Create(View):

    template_name = "article_create.html"

    def init_data(self, block_id):
    	self.block_id = block_id
    	self.block = Block.objects.get(id=block_id)

    def get(self, request, block_id):
    	self.init_data(block_id)
    	return render(request, self.template_name, {"b":self.block})

    def post(self, request, block_id):
    	self.init_data(block_id)

    	#校验器，在/article/forms.py中定义
    	form = ArticleForm(request.POST)
    	
    	if form.is_valid():
    		article = Article(block=self.block, title=form.cleaned_data["title"], content=form.cleaned_data["content"], status=0)
    		article.save()
    		return redirect("/article/list/%s" %self.block_id)
    	
    	else:
    		return render(request, self.template_name, {"b":self.block, "form":form})

