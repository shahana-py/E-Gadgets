from django.shortcuts import render, get_object_or_404
from . models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    featured_products=Product.objects.order_by('priority')[:4]
    latest_products=Product.objects.order_by('-id')[:8]
    context={
        'featured_products':featured_products,
        'latest_products':latest_products
    }
    return render(request,'index.html',context)


def list_products(request):
    """_summary_
    returns product list page
    Args:
    request (_type_):_description_

    returns:
    _type_:_description_
    """
    page=1
    if request.GET:
        page=request.GET.get('page',1)

    product_list=Product.objects.order_by('priority')
    product_paginator=Paginator(product_list,4)
    product_list=product_paginator.get_page(page)
    context={'products':product_list}
    return render(request,'products_list.html',context)

def detail_product(request,product_id):
    product=get_object_or_404(Product,id=product_id)
    context_single={'product':product}
   
    return render(request,'product_detail.html',context_single)

def search(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(title__icontains=query)  # Case-insensitive search
    return render(request, 'search_results.html', {'query': query, 'products': products})


def smartband_des(request):
    return render(request,'smartband_description.html')
