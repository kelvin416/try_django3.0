"""
To render HTML webpages
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article


def home_view(request, *args, **kwargs):

    """
    Take in a request
    Return HTML as a response (We pick to return thhe reponse)
    """

    name = "Kelvin"
    random_id = random.randint(1, 3)
    # From database
    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()
    context = {
        "object_list": article_queryset,
        "object": article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }

    HTML_STRING = render_to_string("home-view.html", context=context)

    # HTML_STRING = """
    # <h1>The title is {title}!</h1>
    # <p>content is {content} (id:{id})</p>
    # """.format(**context)
    return HttpResponse(HTML_STRING)
