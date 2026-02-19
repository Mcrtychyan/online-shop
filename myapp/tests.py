from django.test import TestCase
from .models import Category, Products


class SimpleModelTests(TestCase):
    def test_category_creation(self):
        cat = Category(name='Одежда', slug='clothes')
        cat.save()

        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(cat.name, 'Одежда')

    def test_product_creation(self):
        cat = Category.objects.create(name='Книги', slug='books')

        product = Products.objects.create(
            name='Python для начинающих',
            category_id=cat,
            slug='python-book',
            price=1500.00,
            stock=20
        )

        self.assertEqual(Products.objects.count(), 1)
        self.assertEqual(product.name, 'Python для начинающих')
        self.assertEqual(product.price, 1500.00)

    def test_product_defaults(self):
        cat = Category.objects.create(name='Тест', slug='test')
        product = Products.objects.create(
            name='Тестовый товар',
            category_id=cat,
            slug='test-product',
            price=100
        )

        self.assertEqual(product.stock, 0)  # по умолчанию 0
        self.assertTrue(product.is_active)  # по умолчанию True