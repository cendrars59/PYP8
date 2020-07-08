from django.contrib.auth.models import User
from django.db import models

from catlog.models import Product


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profiles_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


class UserProductsSearch(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user'
    )
    mainProduct = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='mainProduct'
    )
    subProduct = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='subProduct'
    )

    @classmethod
    def get_products(cls, request):
        user_search = (
            cls.objects.filter(user=request.user).only('subProduct').values()
        )
        productids = set()
        for search in user_search:
            productids.add(search['subProduct_id'])
        products = []
        for di in productids:
            products.append(Product.objects.get(id=di))
        return products
