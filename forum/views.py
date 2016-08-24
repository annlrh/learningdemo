#from django.http import HttpResponse
from django.shortcuts import render
from block.models import Block

def index(request):
#   return HttpResponse("Hello world!")
    block_infos = Block.objects.all().order_by("-id")
    return render(request, "index.html", {"blocks":block_infos})
    
