from django.urls import path
from . import views

urlpatterns = [ # 서버IP/mall/
    path('', views.ItemList.as_view()),
    path('<int:pk>/', views.ItemDetail.as_view()),
    path('category/<str:slug>/', views.category_page),
]