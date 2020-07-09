from django.urls import path

from . import views

app_name = "catlog"

urlpatterns = [
    # Url for the detail view of the product
    path("<int:product_id>/", views.detail, name='detail'),
    # Url for the search view
    path("search/", views.search, name='search'),
]
