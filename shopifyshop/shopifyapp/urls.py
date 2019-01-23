from django.urls import path

from shopifyapp.views import OrderView, ProductView


app_name = 'shopifyapp'

urlpatterns = [
    path('products/', ProductView.as_admin_view(), name='products'),
    path('order/place/', OrderView.as_admin_view(), name='place-order'),
    path('orders/', OrderView.as_admin_view(), name='orders'),
]
