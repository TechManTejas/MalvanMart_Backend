from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from product import views as product_views
from ordered_product import views as ordered_product_views
from category import views as category_views
from tag import views as tag_views
from order import views as order_views

router = DefaultRouter()
router.register('product', product_views.ProductModelViewset,
                basename='product')
router.register('order', order_views.OrderModelViewset,
                basename='order')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
