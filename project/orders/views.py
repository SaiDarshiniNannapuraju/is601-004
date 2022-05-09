#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.Cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                        product=item['product'], price=item['price'],
                        quantity=item['quantity'])
            cart.clear()
        return render(request, 'orders/Created.html',
                      {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'form': form})
