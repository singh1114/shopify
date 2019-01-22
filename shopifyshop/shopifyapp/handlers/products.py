"""Product handler files."""

import requests

from shopifyapp.constants import PRIVATE_APP_BASE_URL


class ProductHandler:

    def __init__(self):
        pass

    def get_products(self):
        return requests.get(
            ''.join([PRIVATE_APP_BASE_URL, 'products.json'])).json()

