"""
URLS
"""
from django.urls import path
from .views import ListUILayoutView, ListCategoryView, ListAttributeView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('ui-layout/', ListUILayoutView.as_view(), name="songs-all"),
    path('categories/', ListCategoryView.as_view(), name="categories-all"),
    path('attribute/<int:id>/', ListAttributeView.as_view(), name="attribute-all"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
