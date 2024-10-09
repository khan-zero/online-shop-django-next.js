from tech.models import Hero, Products, DeliverlyArea, NavList, NavbarFooter
from rest_framework import permissions, viewsets
from rest_framework.decorators import permission_classes

from .serializers import HeroSerializer, ProductsSerializer, DeliverlyAreaSerializer, NavListSerializer, NavbarFooterSerializer

class HeroViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ProductsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Hero.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class DeliverlyAreaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DeliverlyArea.objects.all()
    serializer_class = DeliverlyAreaSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class NavListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = NavList.objects.all()
    serializer_class = NavListSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class NavbarFooterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = NavbarFooter.objects.all()
    serializer_class = NavbarFooterSerializer
    permission_classes = [permissions.IsAuthenticated]
