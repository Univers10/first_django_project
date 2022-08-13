from operator import index
from django.shortcuts import render
from .models import Article

# Create your views here.
def home(request):
    list_articles=Article.objects.all()
    context={'liste_article': list_articles}
    return render(request, 'index.html', context)
