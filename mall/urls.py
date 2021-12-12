from django.urls import path
from . import views

urlpatterns = [ # 서버IP/mall/
    path('', views.index),
    path('<int:pk>/', views.single_item_page),
]