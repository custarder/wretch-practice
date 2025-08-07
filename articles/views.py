from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Article

# Create your views here.
def index(request):
    if request.POST:
        title = request.POST["title"]
        content = request.POST["content"]
        Article.objects.create(title=title, content=content)
        return redirect("articles:index")
    else: 
        articles = Article.objects.all().order_by("-id")
        return render(request, "pages/articles.html", {"articles": articles})

def new(request):
    return render(request, "pages/new.html")

def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, "pages/detail.html", {"article": article})