from django.shortcuts import render
from django.http import HttpResponse
from main.models import *


def home(request):
    all_category = Category.objects.all()
    context = {
        "categories": all_category
    }
    return render(request, 'main/home.html', context)


def category(request):
    if 'sub_category' in request.GET:
        sub_category_id = request.GET['sub_category']
        all_product = Product.objects.filter(sub_category_id=sub_category_id)
        context = {
            "products": all_product
        }
        return render(request, 'main/posts.html', context)

    elif 'category' in request.GET:
        category_id = request.GET['category']
        category = Category.objects.get(id=category_id)
        all_product = Product.objects.filter(
            sub_category__category__id=category_id)
        context = {
            "products": all_product,
            "category": category
        }
        return render(request, 'main/posts.html', context)

    else:
        return HttpResponse('404 not found')


def postDetails(request, id):
    product = Product.objects.get(id=id)
    product.views = product.views + 1
    product.save()
    context = {
        'product': product
    }
    return render(request, 'main/details.html', context)
