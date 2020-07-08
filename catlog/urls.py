from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = "catlog"

urlpatterns = [  
    path("<int:product_id>/", views.detail, name='detail'),
    path("search/", views.search, name='search'), 
]
