from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BookViewSet,
    InventoryViewSet,
    CustomerViewSet,
    TransactionViewSet,
    PurchaseViewSet,
    SaleViewSet,
)

router = DefaultRouter()
router.register(r"books", BookViewSet)
router.register(r"inventories", InventoryViewSet)
router.register(r"customers", CustomerViewSet)
router.register(r"transactions", TransactionViewSet)
router.register(r"purchases", PurchaseViewSet)
router.register(r"sales", SaleViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
