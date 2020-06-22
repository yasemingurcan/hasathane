from rest_framework import serializers

from apps.users.models import Customer, Address, BaseOrder, BaseOrderItems, BaseCard, BaseCartItem, Favorite,\
    FavoriteItems


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        field = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        field = '__all__'


class BaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseOrder
        field = '__all__'


class BaseOrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseOrderItems
        field = '__all__'


class BaseCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseCard
        field = '__all__'


class BaseCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseCartItem
        field = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        field = '__all__'


class FavoriteItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItems
        field = '__all__'
