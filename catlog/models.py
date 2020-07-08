from django.db import models

NUTRITION_GRADES = ['a', 'b', 'c', 'd', 'e']


# Create your models here.
class Category(models.Model):
    """[summary]

    Args:
        models ([type]): [description]

    Returns:
        [type]: [description]
    """
    code = models.TextField(unique=True)
    name = models.TextField()
    url = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Store(models.Model):
    """[summary]

    Args:
        models ([type]): [description]

    Returns:
        [type]: [description]
    """
    code = models.TextField(unique=True)
    name = models.TextField()
    url = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        """sumary_line"""
        return self.name


class Brand(models.Model):
    """[summary]

    Args:
        models ([type]): [description]

    Returns:
        [type]: [description]
    """
    code = models.TextField(unique=True)
    name = models.TextField()
    url = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """[summary]

    Args:
        models ([type]): [description]

    Returns:
        [type]: [description]
    """
    code = models.TextField(unique=True)
    name = models.TextField()
    nutrition_grade_fr = models.TextField()
    quantity = models.TextField()
    ingredients_text = models.TextField(default='no descripton')
    ingredients_text_with_allergens_fr = models.TextField(
        default='no descripton'
    )
    url = models.TextField()
    url_images = models.TextField()
    active = models.BooleanField(default=True)
    categories = models.ManyToManyField(
        Category, related_name='products', blank=True
    )
    stores = models.ManyToManyField(Store, related_name='products', blank=True)
    brands = models.ManyToManyField(Brand, related_name='products', blank=True)

    def __str__(self):
        return self.name

    def get_recommanded_products(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        products = []
        for product in Product.objects.filter(
            categories=self.categories.values()[0]['id']
        ):
            if NUTRITION_GRADES.index(
                product.nutrition_grade_fr
            ) <= NUTRITION_GRADES.index(self.nutrition_grade_fr):
                products.append(product)
        return products
