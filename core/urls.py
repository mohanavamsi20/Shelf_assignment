# shape_analyzer/urls.py

from django.urls import path
from .views import analyze_grid,default_success_view

urlpatterns = [
    path('', default_success_view, name='default-success'),
    path('analyze/', analyze_grid, name='analyze-grid'),
]
