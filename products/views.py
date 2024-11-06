from django.shortcuts import render, redirect, get_object_or_404
from . models import Product
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    feature_products=Product.objects.order_by('priority')[:8]
    latest_products=Product.objects.order_by('-id')[:4]
    context={
        'feature_products':feature_products,
        'latest_products':latest_products
    }
    print(context)
    return render(request,'index.html',context)

def list_products(request):
    """_summery
    returns product list page
    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list=Product.objects.order_by('-priority')
    product_paginator=Paginator(product_list,6)
    product_list=product_paginator.get_page(page)
    context={'products':product_list}
    return render(request,'products.html',context)

def detail_product(request,pk):
    product=Product.objects.get(pk=pk)
    context={'product':product}
    return render(request,'product_detail.html',context)

def add_to_cart(request, product_id):
    """Handles adding a product to the shopping cart"""
    if request.method == 'POST':
        size = request.POST.get('size')
        quantity = int(request.POST.get('quantity', 1))
        
        # Get product details from the database
        product = get_object_or_404(Product, pk=product_id)

        # Get the current cart from the session or initialize it
        cart = request.session.get('cart', {})
        
        if product_id in cart:
            cart[product_id]['quantity'] += quantity  # Update quantity if product already in cart
        else:
            # Add new product to the cart
            cart[product_id] = {
                'title': product.title,
                'price': product.price,  # Store the product's price
                'quantity': quantity,
                'image_url': product.image.url if product.image else '',  # Store image URL if it exists
            }
        
        request.session['cart'] = cart  # Save the updated cart back to the session
        
        # Redirect to the cart view in the orders app
        return redirect('orders:cart')  # Update this line

    return redirect('home')