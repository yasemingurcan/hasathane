from rest_framework import viewsets

# Create your views here.
from apps.common.models import HomePage, Footer, FooterItem
from apps.common.serializers import HomePageSerializer, FooterSerializer, FooterItemsSerializer


class HomePageViewSet(viewsets.ModelViewSet):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer


class FooterViewSet(viewsets.ModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer


class FooterItemViewSet(viewsets.ModelViewSet):
    queryset = FooterItem.objects.all()
    serializer_class = FooterItemsSerializer
