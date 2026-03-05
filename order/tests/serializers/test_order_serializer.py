import pytest

from order.serializers import OrderSerializer
from product.factories import ProductFactory


@pytest.mark.django_db
def test_order_serializer_valid():
    product_1 = ProductFactory(price = 10)
    product_2 = ProductFactory(price = 20)
    
    data = {
        "product": [product_1.id, product_2.id]
    }
    
    serializer = OrderSerializer(data = data)
    
    assert serializer.is_valid()
    print(serializer.errors)