from django.shortcuts import render
from . models import Item

# Create your views here.
def index(request):
    items = Item.objects.all().order_by('-pk')

    return render(request, 'mall/index.html',
                  {
                      'items' : items
                  }
                  )

def single_item_page(request, pk):
    item = Item.objects.get(pk=pk)

    return render(request, 'mall/single_item_page.html',
                  {
                      'item' : item
                  }
                  )
