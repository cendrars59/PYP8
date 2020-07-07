from django.urls import path
from django.views.generic import TemplateView
from django.urls import path
from . import views 


app_name = "catlog"

urlpatterns = [
    path("", views.catalogue, name="catalogue"),
    path("<int:product_id>/", views.detail, name='detail'),
    path("search/", views.search, name='search'),
    
]
