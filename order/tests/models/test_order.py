import pytest

from order.factories import OrderFactory


@pytest.mark.django_db
def test_create_order():
    order = OrderFactory
    
    assert order.product is not None
    assert order.user is not None
