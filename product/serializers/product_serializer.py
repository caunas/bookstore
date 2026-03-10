from rest_framework import serializers

from product.models import Product
from product.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(required = True, many = True)

    categories_id = serializers.PrimaryKeyRelatedField(
            queryset=Categor.objects.all(),
            write_only = True,
            many = True
            )
    
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'active',
            'categories',
        ]



    def create(self, validated_data):
        category_data = validated_data.pop("categories_id")

        product = Product.objects.create(**validated_data)
        for category in category_data:
            product.category.add(category)


        return product
