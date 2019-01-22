import requests

from shopifyapp.constants import PRIVATE_APP_BASE_URL


class OrderHandler:

    def __init__(self):
        self.order_url = ''.join([PRIVATE_APP_BASE_URL, 'orders.json'])

    def place_order(self, variant_id, quantity):
        """Place order for the variant id and quantity."""
        order_data = {
            'order': {
                'line_items': [
                    {
                        'quantity': quantity,
                        'variant_id': variant_id
                    }
                ]
            }
        }
        return requests.post(self.order_url, json=order_data).json()

    def get_orders(self):
        """Get all orders for the app."""
        return requests.get(self.order_url).json()
