import pytest

from product.factories import CategoryFactory


@pytest.fixture
def category_created():
    return CategoryFactory(title = "CATEGORY FACTORIED")


@pytest.mark.django_db
def test_create_category(category_created):
    assert category_created.title == "CATEGORY FACTORIED"