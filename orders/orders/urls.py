from api.views import *
from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from django_rest_passwordreset.views import reset_password_confirm, reset_password_request_token
router = routers.SimpleRouter()
router.register(r'user', UserViewSet)
router.register(r'product', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/register', RegisterUser.as_view()),
    path('api/v1/', include(router.urls)),
    path('user/register/confirm', Сonfirmation.as_view()),
    path('user/login', LoginUser.as_view()),
    path('user/contact', ContactView.as_view()),
    path('user/contacts', ContactAPIList.as_view()),
    path('user/details', DetailUser.as_view()),
    path('user/passwordreset', reset_password_request_token),
    path('user/passwordreset/confirm', reset_password_confirm),
    path('shops', ShopView.as_view()),
    path('categories', CategoryView.as_view()),
    path('products', ProductView.as_view()),
    path('partner/update', PartnerUpdate.as_view()),
    path('partner/state', PartnerState.as_view()),
    path('partner/qwer', PartnerOrders.as_view()),
    path('cart', CartView.as_view()),
    path('order', OrderView.as_view()),
]