from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Article
from django.contrib import messages

# Create your views here.
def index(request):
    messages.success(request, "新增成功！！")
    if request.POST:
        title = request.POST["title"]
        content = request.POST["content"]
        Article.objects.create(title=title, content=content)
        messages.success(request, "新增成功")
        return redirect("articles:index")
    else: 
        articles = Article.objects.all().order_by("-id")
        return render(request, "pages/articles.html", {"articles": articles})

def new(request):
    return render(request, "pages/new.html")

def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    if request.POST:
         if request.POST["_method"] == "patch":
              title = request.POST["title"]
              content = request.POST["content"]
              article.title = title
              article.content = content
              article.save()
              messages.success(request, "更新成功")
              return redirect("articles:detail", article.id)
         if request.POST["_method"] == "delete":
              article.delete()
              messages.success(request, "刪除成功")
              return redirect("articles:index")
    else:
        return render(request, "pages/detail.html", {"article": article})

def edit(request, id):
        article = get_object_or_404(Article, pk=id)
        return render(request, "pages/edit.html", {"article": article})