from django.shortcuts import render
from django.http import HttpResponse
from main.models import Product, Location


def product_search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(title__icontains=query)
    cities = Location.objects.filter(type='city')
    divisions = Location.objects.filter(type='division')

    context = {
        "products": products,
        "cities": cities,
        "divisions": divisions,
        "query": query
    }
    return render(request, 'main/posts.html', context)
