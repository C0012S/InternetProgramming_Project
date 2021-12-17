from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . models import Item, Category, Comment
from django.core.exceptions import PermissionDenied
from . forms import CommentForm
from django.shortcuts import get_object_or_404
from django.db.models import Q

class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(CommentUpdate, self).dispatch(request, *args, **kwargs)
        else:
            return PermissionDenied

def new_comment(request, pk):
    if request.user.is_authenticated:
        item = get_object_or_404(Item, pk=pk)
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.item = item
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else:
            return redirect(item.get_absolute_url())
    else:
        raise PermissionDenied

# Create your views here.
class ItemCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Item
    fields = ['item_name', 'item_explanation', 'item_price', 'item_size', 'item_material', 'category'] # item_image, maker 추가 필요

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(ItemCreate, self).form_valid(form)
        else:
            return redirect('/mall/')

class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['item_name', 'item_explanation', 'item_price', 'item_size', 'item_material', 'category']  # item_image, maker 추가 필요

    template_name = 'mall/item_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser): # 로그인한 staff와 superuser라면
            return super(ItemUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

class ItemList(ListView) :
    model = Item
    ordering = '-pk'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ItemList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_item_count'] = Item.objects.filter(category=None).count()
        return context

# item_list.html

class ItemDetail(DetailView) :
    model = Item

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ItemDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_item_count'] = Item.objects.filter(category=None).count()
        context['comment_form'] = CommentForm
        return context

# item_detail.html

class ItemSearch(ItemList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        item_list = Item.objects.filter(
            Q(item_name__contains = q) | Q(item_explanation__contains = q)
        ).distinct()
        return item_list

    def get_context_data(self, **kwargs):
        context = super(ItemSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search : {q}({self.get_queryset().count()})'

        return context

def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        item_list = Item.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        item_list = Item.objects.filter(category=category)
    return render(request, 'mall/item_list.html',
                  {
                      'item_list' : item_list,
                      'categories' : Category.objects.all(),
                      'no_category_item_count' : Item.objects.filter(category=None).count(),
                      'category' : category
                  }
                  )
