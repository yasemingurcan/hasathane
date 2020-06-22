from rest_framework import viewsets
from apps.users.models import Customer, Address, BaseOrder, Favorite, FavoriteItems, BaseCard
from apps.users.serializers import CustomerSerializer, AddressSerializer, BaseOrderSerializer,\
    FavoriteSerializer, FavoriteItemsSerializer, BaseCardSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class BaseOrderViewSet(viewsets.ModelViewSet):
    queryset = BaseOrder.objects.all()
    serializer_class = BaseOrderSerializer


class BaseCardViewSet(viewsets.ModelViewSet):
    queryset = BaseCard.objects.all()
    serializer_class = BaseCardSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


class FavoriteItemsViewSet(viewsets.ModelViewSet):
    queryset = FavoriteItems.objects.all()
    serializer_class = FavoriteItemsSerializer
