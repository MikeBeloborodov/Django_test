from django.http import HttpResponse
from articles.models import Article


def home_view(request):
    obj = Article.objects.get(id=1)
    HTML_STRING = f"""
    <h1>Hello world!</h1>
    <p>Title - {obj.title}</p>
    <p>Content - {obj.content}</p>
    <p>ID - {obj.id}</p>
    """
    return HttpResponse(HTML_STRING)