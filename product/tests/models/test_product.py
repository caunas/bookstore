import pytest

from product.factories import ProductFactory


@pytest.fixture
def product_created():
    return ProductFactory(title = "PRODUCT FACTORIED")


@pytest.mark.django_db
def test_create_product(product_created):
    assert product_created.title == "PRODUCT FACTORIED"