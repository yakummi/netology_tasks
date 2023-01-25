from rest_framework import serializers
from .models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'products', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)

        for position in positions:
            stock_product = StockProduct(stock=stock,
                                         product=position.get('product'),
                                         quantity=position.get('quantity'),
                                         price=position.get('price'))

        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)

        for position in positions:
            product = position.get('product')
            quantity = position.get('quantity')
            price = position.get('price')

            obj, created = StockProduct.objects.update_or_create(
                stock=stock,
                product=product,
                defaults={'price': price,
                          'quantity': quantity}
            )

        return stock