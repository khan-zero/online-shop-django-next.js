from rest_framework import serializers
from tech.models import Hero, Products, DeliverlyArea, NavList, NavbarFooter, NavbarFooter

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'
        
class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        
class DeliverlyAreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeliverlyArea
        fields = '__all__'
        
class NavListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NavList
        fields = '__all__'
        
class NavbarFooterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NavList
        fields = '__all__'
