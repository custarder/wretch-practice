from django.shortcuts import render

def about(request):
    return render(request, "pages/about.html")

def contact(request):
    return render(request, "pages/contact.html")

def home(request):
    secret_word = [1,2,4,12,124]
    return render(request, "pages/home.html", {"secret_word": secret_word})

