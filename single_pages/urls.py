from django.urls import path
from . import views

urlpatterns = [ # 서버IP/
    path('', views.home_page),    # 서버IP/
    path('my_page/', views.my_page),   # 서버IP/my_page/
    path('about_company/', views.about_company),   # 서버IP/about_company/
]
