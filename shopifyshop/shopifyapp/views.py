from django.shortcuts import render

from base.views import BaseAdminView

from shopifyapp.handlers.orders import OrderHandler
from shopifyapp.handlers.products import ProductHandler


class ProductView(BaseAdminView):
    """Product related views."""

    def get(self, request, *args, **kwargs):
        products = ProductHandler().get_products()
        return render(request, 'shopifyapp/products.html', {
            'products': products,
        })


class OrderView(BaseAdminView):
    """Order view to place an order."""

    def get(self, request, *args, **kwargs):
        orders = OrderHandler().get_orders()
        return render(request, 'shopifyapp/orders.html', {
            'orders': orders,
        })

    def post(self, request, *args, **kwargs):
        quantity = int(request.POST.get('quantity'))
        variant_id = int(request.POST.get('variant_id'))
        product_title = request.POST.get('product_title')
        OrderHandler().place_order(variant_id, quantity)
        return render(request, 'shopifyapp/order-placed.html', {
            'item_brought': product_title,
            'quantity': quantity
        })
