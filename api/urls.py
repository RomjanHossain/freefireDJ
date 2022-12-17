from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import (BuyHistoryAPIView, BuyListAPIView, CarasolModelListAPIView,
                    ContactUsListAPIView, ItemsListAPIView, LogoutAPIView,
                    PaymentMethodListAPIView, ProfileAPIView, RegisterAPIView,
                    ServicesListAPIView, UpdateProfileAPIView)

urlpatterns = [
    # user stuff
    path("login/", obtain_auth_token, name="login"),
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("profile/", ProfileAPIView.as_view(), name="profile"),
    path("update/<pk>/", UpdateProfileAPIView.as_view(), name="update"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    # landing stuff
    path("carasol/", CarasolModelListAPIView.as_view(), name="carasol"),
    path("services/", ServicesListAPIView.as_view(), name="services"),
    path("items/", ItemsListAPIView.as_view(), name="items"),
    path("payment/", PaymentMethodListAPIView.as_view(), name="payment"),
    path("buy/", BuyListAPIView.as_view(), name="buy"),
    path("buy-history/", BuyHistoryAPIView.as_view(), name="buy-history"),
    path("contact/", ContactUsListAPIView.as_view(), name="contact"),
]
