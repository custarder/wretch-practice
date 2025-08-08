from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Article
from django.contrib import messages
from .forms import ArticleForm

# Create your views here.
def index(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        form.save()
        messages.success(request, "新增成功")
        return redirect("articles:index")
    else: 
        articles = Article.objects.order_by("-id")
        return render(request, "pages/articles.html", {"articles": articles})

def new(request):
    form = ArticleForm()
    return render(request, "pages/new.html", {"form": form})

def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    if request.POST:
         if request.POST["_method"] == "patch":
            form = ArticleForm(request.POST, instance=article)
            form.save()
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
        form = ArticleForm(instance=article)
        return render(request, "pages/edit.html", {"article": article, "form": form})