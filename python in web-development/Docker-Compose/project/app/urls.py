from rest_framework.routers import DefaultRouter

from app.views import ProductViewSet, StockViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = router.urls