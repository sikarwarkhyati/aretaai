from django.urls import path
from . import views

urlpatterns = [
    path('query/', views.query_view, name='query_view'),
    path('result/', views.result_view, name='result_view'),
]