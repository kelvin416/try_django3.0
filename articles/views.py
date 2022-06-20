from multiprocessing import context
from django.shortcuts import render
from .models import Article

# Create your views here.

def article_search_view(request):
    query_dict = request.GET #this is a dictionary
    # query = query_dict.get("q") #<input type="text" name="q"> from base.html

    try:
        query = int(query_dict.get("q"))
    except:
        query = None
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {
        "object": article_obj
    }
    return render(request, "articles/search.html", context)

def article_detail_view(request, id=None):
    article_obj =None
    if id is not None:
        article_obj = Article.objects.get(id=id)

    context = {
        "object": article_obj
    }
    return render(request, "articles/detail.html", context)
 
