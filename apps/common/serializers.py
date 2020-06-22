from rest_framework import serializers

from apps.common.models import HomePage, Footer, FooterItem


class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = ['id', 'name', 'type', 'order']


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'


class FooterItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterItem
        fields = '__all__'
