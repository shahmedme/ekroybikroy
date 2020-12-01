from django.http.response import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.db.models import Q
from django.views.generic import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from main.models import *
from account.models import *


def home(request):
    if request.method == 'GET':
        all_category = Category.objects.all()

        context = {
            "categories": all_category,
        }
        return render(request, 'main/home.html', context)


def posts(request):
    cities = Location.objects.filter(type='city')
    divisions = Location.objects.filter(type='division')

    context = {
        'cities': cities,
        'divisions': divisions
    }

    if 'sub_category' in request.GET:
        id = request.GET.get('sub_category')
        sub_category = SubCategory.objects.get(
            id=id)
        products = Product.objects.filter(
            sub_category=sub_category).order_by('-created_at')

        page = request.GET.get('page', 1)
        paginator = Paginator(products, 5)

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        snip = '&sub_category={}'.format(id)

        context['products'] = products
        context['snip'] = snip

    elif 'category' in request.GET:
        id = request.GET.get('category')
        category = Category.objects.get(id=id)
        products = Product.objects.filter(
            sub_category__category=category).order_by('-created_at')

        page = request.GET.get('page', 1)
        paginator = Paginator(products, 5)

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        snip = '&category={}'.format(id)

        context['products'] = products
        context['snip'] = snip

    elif 'userid' in request.GET:
        user_id = request.GET['userid']
        products = Product.objects.filter(seller_id=user_id)

        context['products'] = products

    else:
        products = Product.objects.all().order_by('-created_at')
        page = request.GET.get('page', 1)
        paginator = Paginator(products, 5)

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context['products'] = products

    return render(request, 'main/posts.html', context)


def post_details(request, product_slug):
    try:
        product = Product.objects.get(slug=product_slug)
        product.views = product.views + 1
        product.save()

        context = {
            'product': product
        }
        return render(request, 'main/details.html', context)
    except Product.DoesNotExist:
        raise Http404


# def c_signup(request):
#     # if request == 'GET': Otp confirmation part backend i did not solved.
#     return render(request, 'main/signup-confirm.html')

#     if request.method == 'POST':
#         # otp = request.POST['otp'] This time we dont need otp.
#         password = request.POST['password']
#         c__password = request.POST['c__password']

#         nxt_customer = Customer_details(
#             password=password, c_password=c__password)
#         nxt_customer.save()
#         return redirect('/')


@login_required(login_url='/login')
def action_handler(request):
    action = request.GET.get('action')

    if action == 'get-subcategory':
        category_id = request.GET.get('id')
        subcategories = SubCategory.objects.filter(category_id=category_id)
        subcategory_list = list(subcategories.values())

        return JsonResponse(subcategory_list, safe=False)

    elif action == 'get-areas':
        location_id = request.GET.get('id')
        areas = Location.objects.filter(parent_id=location_id)
        area_list = list(areas.values())

        return JsonResponse(area_list, safe=False)


@login_required(login_url='/login')
def add_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        price = request.POST.get("price")
        is_negotiable = True if request.POST.get("negotiable") == 'on' else False
        condition = request.POST.get('condition')
        photos = request.FILES.getlist('files')
        subcategory = SubCategory.objects.get(id=request.POST.get("subcategory"))
        phone = request.POST.get("phone")
        location = Location.objects.get(id=request.POST.get('area'))

        product = Product.objects.create(title=title, sub_category=subcategory, condition=condition, contact=phone, price=price, description=description,
                                         is_negotiable=is_negotiable, location=location, seller=request.user)

        is_primary = True
        for photo in photos:
            Photo.objects.create(
                file=photo, product=product, is_primary=is_primary)
            is_primary = False
        return redirect("/")

    else:
        categories = Category.objects.all()
        locations = Location.objects.filter(
            Q(type="city") | Q(type="division")).distinct()
        context = {
            'categories': categories,
            'locations': locations,
        }

        return render(request, 'main/addposts.html', context)


def setup_site(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        tagline = request.POST.get('tagline')
        email = request.POST.get('email')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        SiteInfo.objects.create(name=name, tagline=tagline, email=email,
                                address=address, contact=contact)

        return redirect('/')


def not_found(request):
    return render(request, 'main/404.html')


def handler404(request, exception):
    return render(request, 'main/404.html', status=404)
