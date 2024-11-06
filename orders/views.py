from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from django.contrib import messages
from products.models import Product

def cart(request):
    cart = request.session.get('cart', {})
    
    # Initialize subtotal, tax, and total
    subtotal = 0
    cart_items = []

    if not cart:
        messages.info(request, "Your cart is empty.")

    for product_id, details in cart.items():
        price = details.get('price', 0)
        quantity = details.get('quantity', 1)
        item_total = price * quantity
        subtotal += item_total
        
        # Add item details with the total to the cart_items list
        cart_items.append({
            'product_id': product_id,
            'title': details.get('title', 'Unknown Product'),
            'price': price,
            'quantity': quantity,
            'item_total': item_total,
            'image_url': details.get('image_url', ''),
        })

    tax = subtotal * 0.07  # Assuming 7% tax
    total = subtotal + tax
    
    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'tax': tax,
        'total': total,
    }
    return render(request, 'cart.html', context)

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)  # Convert product_id to string for consistency
    if product_id in cart:
        del cart[product_id]
        messages.success(request, "Product removed from cart.")
    else:
        messages.warning(request, "Product not found in cart.")
    request.session['cart'] = cart
    return redirect('orders:cart')

def checkout_view(request):
    # Your checkout logic here
    return render(request, 'checkout.html') 