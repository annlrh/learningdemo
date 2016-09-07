from django.core.paginator import Paginator

#Article_CNT_1page为每页显示的文章数，half_show_length为页面显示页码数的一半
def paginate_queryset(all_articles, page_no, Article_CNT_1page=1, half_show_length=3):

	#分页器实例
	p = Paginator(all_articles, Article_CNT_1page)

	if page_no > p.num_pages:
		page_no = p.num_pages
	if page_no <= 0:
		page_no = 1

	#当前页面实例
	page = p.page(page_no)

	#生成文章列表分页实例
	article_objs = page.object_list

	#页面显示的页码list
	page_links = [i for i in range(page_no-half_show_length, page_no+half_show_length+1) if i>0 and i<=p.num_pages]

	pagination_data = {"current_no": page_no,  #当前页码
						"page_links": page_links, #页码list
						"page_cnt": p.num_pages, #总页数
						"previous_link": page_links[0]-1, #最小页码-1
						"next_link": page_links[-1]+1, #最大页码+1
						"has_previous": page_links[0] > 1, #最小页码前面是否还有页
						"has_next": page_links[-1] <= p.num_pages-1 #最大页码后面是否还有页

	}

	return(article_objs, pagination_data)