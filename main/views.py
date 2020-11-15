from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import View

from main.models import *
from account.models import *


def home(request):
    if request.method == 'GET':
        all_category = Category.objects.all()

        context = {
            "categories": all_category,
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
def add_post(request):
    if "action" in request.GET and request.is_ajax:
        action = request.GET.get("action")
        if action == 'get-locations':
            id = request.GET.get('id').split('-')
            if id[0] == "d":
                districts = District.objects.filter(division_id=id[1]).values()
                districts_list = list(districts)
                return JsonResponse(districts_list, safe=False)
            elif id[0] == "c":
                areas = Area.objects.filter(city_id=id[1]).values()
                areas_list = list(areas)
                return JsonResponse(areas_list, safe=False)
        elif action == 'get-subcategory':
            id = request.GET.get('id')
            subcategories = SubCategory.objects.filter(category_id=id).values()
            subcategory_list = list(subcategories)
            return JsonResponse(subcategory_list, safe=False)

    elif request.method == "POST":
        title = request.POST["title"]
        subcategory = SubCategory.objects.get(id=request.POST["subcategory"])
        thumbnail = request.FILES['thumbnail']
        price = request.POST["price"]
        checkbox = request.POST.getlist("checkbox")
        phone_no = request.POST["phone_no"]
        division_city = request.POST["division-city"].split('-')
        district_area = request.POST["district-area"]
        address = request.POST["address"]
        desc = request.POST["description"]
        is_negotiable = False

        if "checked" in checkbox:
            is_negotiable = True

        if division_city[0] == "d":
            location = Location(district_id=district_area)
            location.save()

        elif division_city[0] == "c":
            location = Location(area_id=district_area)
            location.save()

        add_post = Product(title=title, sub_category=subcategory, address=address, contact=phone_no, price=price, desc=desc,
                           thumbnail=thumbnail, is_negotiable=is_negotiable, location=location, seller=request.user.profile)
        add_post.save()
        return redirect("/")

    else:
        categories = Category.objects.all()
        divisions = Division.objects.all()
        cities = City.objects.all()
        context = {
            'categories': categories,
            'divisions': divisions,
            'cities': cities
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
