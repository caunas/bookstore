import pytest

from product.serializers import CategorySerializer
from product.factories import CategoryFactory


@pytest.fixture
def category_created():
    return CategoryFactory(slug="fab")


@pytest.mark.django_db
def test_category_serializer(category_created):
    serializer = CategorySerializer(category_created)

    data = serializer.data

    assert data["slug"] == "fab"


@pytest.mark.django_db
def test_category_serializer_valid():
    data = {
        "title":  "FABRICADOS",
        "slug": "fab",
        "description": "CATEGORIA FABRICADA",
        "active": False,
    }
    
    serializer = CategorySerializer(data = data)
    
    assert serializer.is_valid()