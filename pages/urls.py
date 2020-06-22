from django.urls import path
from django.views.generic import TemplateView
from django.urls import path
from . import views 

urlpatterns = [
    path("", views.home, name="pages-home"),
    path("mentions", views.mentions, name="pages-mentions"),
]
