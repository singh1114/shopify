"""Constants for shopify app file."""

import os


PRIVATE_APP_BASE_URL = (
    'https://{}:{}@misshopmashup.myshopify.com/admin/'.format(
        os.environ['PRIVATE_SHOPIFY_API_KEY'],
        os.environ['PRIVATE_SHOPIFY_PASSWORD']
    )
)

