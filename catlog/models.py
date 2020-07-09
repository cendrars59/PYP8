from django.db import models

NUTRITION_GRADES = ['a', 'b', 'c', 'd', 'e']


# Create your models here.
class Category(models.Model):
    """Class managing any element regarding category object

    Args:
        models ([type]): [description]

    Returns:
        Category: Return an object of type Category
    """

    code = models.TextField(unique=True)
    name = models.TextField()
    url = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        """ Return the name of category instead of technical description

        Returns:
            String: Name of the category
        """
        return self.name


class Store(models.Model):
    """Class managing any element regarding store object

    Args:
        models ([type]): [description]

    Returns:
        Store: Return an object of type Store
    """

    code = models.TextField(unique=True)
    name = models.TextField()
    url = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        """ Return the name of brand instead of technical description

        Returns:
            String: Name of the store
        """
        return self.name


class Brand(models.Model):
    """Class managing any element regarding brand object

    Args:
        models ([type]): [description]

    Returns:
        Brand: Return an object of type Brand
    """

    code = models.TextField(unique=True)
    name = models.TextField()
    url = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        """ Return the name of brand instead of technical description

        Returns:
            String: Name of the brand
        """
        return self.name


class Product(models.Model):
    """[Class managing any element regarding product object]

    Args:
        models ([type]): [description]

    Returns:
        [Product]: [Return an object of type Product]
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
        """ Return the name of product instead of technical description

        Returns:
            String: Name of the product
        """
        return self.name

    def get_recommanded_products(self):
        """Get the list of recommanded products according the nutrition grade
        of the current product. Only products having same grade or better are
        part of the results

        Returns:
            List: List of products
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
