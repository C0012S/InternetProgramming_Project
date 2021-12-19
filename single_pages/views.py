from django.shortcuts import render
from mall.models import Item, Category, Maker

# Create your views here.

def home_page(request):
    recent_items = Item.objects.order_by('-pk')[:3]
    return render(request, 'single_pages/home_page.html',
                  {'recent_items' : recent_items})

def my_page(request):
    item_list = Item.objects.order_by('-pk')
    return render(request, 'single_pages/my_page.html',
                  {'item_list' : item_list})

def about_company(request):
    category = Category.objects.all()

    maker = Maker.objects.all()

    item_list = Item.objects.order_by('-pk')
    return render(request, 'single_pages/about_company.html',
                  {'category' : category,
                   'item_list' : item_list,
                   'maker' : maker})
