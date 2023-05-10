from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomeAPI.as_view(), name='home'),
    path('category/<slug:slug>', CategoryAPIDetailView.as_view(), name='category'),
    path('product/<slug:slug>', Product_detail.as_view(), name='product_detail'),
    path('login/', include('rest_framework.urls')), #сессионный токен
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('checkout/', checkout, name='checkout'),
    path('order/<int:order_id>/', order_detail, name='order_detail'),
    path('profile/', profile, name='profile'),
    path('orders/', order_history, name='order_history'),
    path('register/', register, name='register'),
    path('payment/', payment, name='payment'),
    path('search/', search, name='search'),
    path('contacts/', kontakti, name='contacts'),
    path('cart/', cart, name='cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
