from django.contrib import admin
from django.views import View

from rest_framework.views import APIView


class BaseView(APIView):
    """Base view class to handle all view operations."""

    pass


class BaseAdminView(View):

    @classmethod
    def as_admin_view(cls):
        """Add as_admin_view with Admin View."""
        view = cls.as_view()
        admin_site = admin.site
        return admin_site.admin_view(view)

