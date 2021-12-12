from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'single_pages/home_page.html')

def my_page(request):
    return render(request, 'single_pages/my_page.html')

def about_company(request):
    return render(request, 'single_pages/about_company.html')
