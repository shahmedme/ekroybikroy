from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def posts(request):
    return render(request, 'main/post.html')
