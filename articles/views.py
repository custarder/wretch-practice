from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    if request.POST:
        title = request.POST["title"]
        content = request.POST["content"]
        Article.objects.create(title=title, content=content)
        return redirect("pages:home")
    else: 
        return render(request, "pages/articles.html")

def new(request):
    return render(request, "pages/new.html")