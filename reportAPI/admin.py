"""
reportAPI
"""
# Register your models here.

from django.contrib import admin
from .models import UILayout, Category, Association, Attribute

admin.site.register(UILayout)
admin.site.register(Category)
admin.site.register(Association)
admin.site.register(Attribute)
admin.site.site_header = 'Zealian administration'