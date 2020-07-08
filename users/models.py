from django.db import models
from django.contrib.auth.models import User
from catlog.models import Product



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profiles_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    

class UserProductsSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mainProduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='mainProduct')
    subProduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='subProduct')
    