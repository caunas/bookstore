import pytest

from product.models import Product,Category
from product.serializers import ProductSerializer

pytestmark = pytest.mark.django_db


def test_product_serializer():
    category = Category.objects.create(
        title =  "FABRICADOS",
        slug = "fab",
        description =  "CATEGORIA FABRICADA",
        active = True,
    )
    
    product = Product.objects.create(
        title = "FABRICADO",
        description = "PRODUTO FABRICADO",
        price = 100,
        active = True,
    )
    
    product.categories.add(category)
    serializer = ProductSerializer(product)
    data = serializer.data
    
    assert data["title"] == "FABRICADO"
    assert data["categories"][0]["slug"] == "fab"
