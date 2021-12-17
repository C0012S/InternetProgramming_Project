from django.shortcuts import render
from mall.models import Item

# Create your views here.

def home_page(request):
    recent_items = Item.objects.order_by('-pk')[:3]
    return render(request, 'single_pages/home_page.html',
                  {'recent_items' : recent_items})

def my_page(request):
    return render(request, 'single_pages/my_page.html')

def about_company(request):
    return render(request, 'single_pages/about_company.html')
