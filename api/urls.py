from django.urls import include, path
from rest_framework import routers
from .views import HeroViewSet, ProductsViewSet, DeliverlyAreaViewSet, NavListViewSet, NavbarFooterViewSet

router = routers.DefaultRouter()
router.register(r'hero', HeroViewSet, basename='hero')
router.register(r'product', ProductsViewSet, basename='product')
router.register(r'deliver', DeliverlyAreaViewSet, basename='deliverlyarea')
router.register(r'navlist', NavListViewSet, basename='navlist')
router.register(r'navfooter', NavbarFooterViewSet, basename='navbarfooter')

urlpatterns = [
    path('', include(router.urls)),
]

