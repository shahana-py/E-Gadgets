from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('products_list/', views.list_products,name='list_product'),
    path('product/<int:product_id>/', views.detail_product,name='detail_product'),
    path('search/', views.search, name='search'),
   
    path('smartband/', views.smartband_des,name='smartband'),
]
