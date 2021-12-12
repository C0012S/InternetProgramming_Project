from django.shortcuts import render
from django.views.generic import ListView, DetailView

from . models import Item

# Create your views here.
class ItemList(ListView) :
    model = Item
    ordering = '-pk'
#    template_name = 'mall/index.html'
# item_list.html

class ItemDetail(DetailView) :
    model = Item
# item_detail.html

# def index(request):
#     items = Item.objects.all().order_by('-pk')
#
#     return render(request, 'mall/index.html',
#                   {
#                       'items' : items
#                   }
#                   )
#
# def single_item_page(request, pk):
#     item = Item.objects.get(pk=pk)
#
#     return render(request, 'mall/single_item_page.html',
#                   {
#                       'item' : item
#                   }
#                   )
