from django.shortcuts import render, redirect
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
    return render(request, "pages/detail.html", {"id": id})