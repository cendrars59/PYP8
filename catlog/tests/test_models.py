from django.test import TestCase

from catlog.models import Brand, Category, Product


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Product.objects.create(
            code='dummy_code',
            name='Dummy Product',
            nutrition_grade_fr='e',
            quantity='200 gr',
            ingredients_text='Dummy ingredient text',
            ingredients_text_with_allergens_fr='Dummy ingredient text fr',
            url='Dummy url',
            url_images='Dummy url images',
            active=True,
        )

    def test_code(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('code').verbose_name
        self.assertEquals(field_label, 'code')

    def test_name(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_grade(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field(
            'nutrition_grade_fr'
        ).verbose_name
        self.assertEquals(field_label, 'nutrition grade fr')

    def test_qty(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('quantity').verbose_name
        self.assertEquals(field_label, 'quantity')

    def test_ingredients(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('ingredients_text').verbose_name
        self.assertEquals(field_label, 'ingredients text')

    def test_ingredients_fr(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field(
            'ingredients_text_with_allergens_fr'
        ).verbose_name
        self.assertEquals(field_label, 'ingredients text with allergens fr')

    def test_url(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('url').verbose_name
        self.assertEquals(field_label, 'url')

    def test_url_images(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('url_images').verbose_name
        self.assertEquals(field_label, 'url images')

    def test_active(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('active').verbose_name
        self.assertEquals(field_label, 'active')

    def test_object_name_is_name(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.name}'
        self.assertEquals(expected_object_name, str(product))


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(
            code='dummy_code',
            name='Dummy Product',
            url='Dummy url',
            active=True,
        )

    def test_code(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('code').verbose_name
        self.assertEquals(field_label, 'code')

    def test_name(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_url(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('url').verbose_name
        self.assertEquals(field_label, 'url')

    def test_active(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('active').verbose_name
        self.assertEquals(field_label, 'active')

    def test_object_name_is_name(self):
        category = Category.objects.get(id=1)
        expected_object_name = f'{category.name}'
        self.assertEquals(expected_object_name, str(category))


class BrandModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Brand.objects.create(
            code='dummy_code',
            name='Dummy Product',
            url='Dummy url',
            active=True,
        )

    def test_code(self):
        brand = Brand.objects.get(id=1)
        field_label = brand._meta.get_field('code').verbose_name
        self.assertEquals(field_label, 'code')

    def test_name(self):
        brand = Brand.objects.get(id=1)
        field_label = brand._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_url(self):
        brand = Brand.objects.get(id=1)
        field_label = brand._meta.get_field('url').verbose_name
        self.assertEquals(field_label, 'url')

    def test_active(self):
        brand = Brand.objects.get(id=1)
        field_label = brand._meta.get_field('active').verbose_name
        self.assertEquals(field_label, 'active')

    def test_object_name_is_name(self):
        brand = Brand.objects.get(id=1)
        expected_object_name = f'{brand.name}'
        self.assertEquals(expected_object_name, str(brand))
