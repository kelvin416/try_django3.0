"""
To render HTML webpages
"""
import random
from django.http import HttpResponse
from articles.models import Article


def home_view(request):

    """
    Take in a request
    Return HTML as a response (We pick to return thhe reponse)
    """

    name = "Kelvin"
    random_id = random.randint(1, 3)
    # From database
    article_obj = Article.objects.get(id=random_id)

    HTML_STRING = f"""
    <h1>The title is {article_obj.title} and content is {article_obj.content} (id:{article_obj.id})!</h1>
    """
    return HttpResponse(HTML_STRING)
