from django.urls import path
from . import views

urlpatterns = [ # 서버IP/mall/
    path('', views.ItemList.as_view()),
    path('<int:pk>/', views.ItemDetail.as_view()),
    path('category/<str:slug>/', views.category_page),
    path('create_item/', views.ItemCreate.as_view()),
    path('update_item/<int:pk>/', views.ItemUpdate.as_view()),
    path('<int:pk>/new_comment/', views.new_comment),
]