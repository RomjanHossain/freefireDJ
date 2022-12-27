from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import (BuyCreateAPIView, BuyHistoryAPIView, BuyListAPIView,
                    CarasolModelListAPIView, ChangePasswordView,
                    CustomAuthToken, GetDialog, GetPaymentMethod,
                    GetSingleItemView, GetSingleService, ImageUploadView,
                    ItemsListAPIView, LogoutAPIView, PaymentMethodListAPIView,
                    ProfileAPIView, ProfilePictureAPIView, RegisterAPIView,
                    ServicesListAPIView, UpdateProfileAPIView, image_detail,
                    image_upload)

urlpatterns = [
    # user stuff CustomAuthToken
    path("login/", obtain_auth_token, name="login"),
    # path("login2/", CustomAuthToken.as_view(), name="login"),
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("profile/", ProfileAPIView.as_view(), name="profile"),
    path("update/<pk>/", UpdateProfileAPIView.as_view(), name="update"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path(
        "change-password/",
        ChangePasswordView.as_view(),
        name="change-password",
    ),
    # upload image
    # path("upload-image/", ProfilePictureAPIView.as_view(), name="upload-image"),
    path("upload-images/", ImageUploadView.as_view(), name="image_upload"),
    path("get-images/", image_detail, name="image_detail"),
    # landing stuff
    path("carasol/", CarasolModelListAPIView.as_view(), name="carasol"),
    path("services/", ServicesListAPIView.as_view(), name="services"),
    path("service/<pk>/", GetSingleService.as_view(), name="service-detail"),
    path("items/<pk>/", ItemsListAPIView.as_view(), name="items"),
    path("get-single-item/<pk>/", GetSingleItemView.as_view(), name="get-item"),
    path("payment-method/<pk>", PaymentMethodListAPIView.as_view(), name="payment"),
    path("payment/", PaymentMethodListAPIView.as_view(), name="payment"),
    path("buy/", BuyListAPIView.as_view(), name="buy"),
    path("order/", BuyCreateAPIView.as_view(), name="order"),
    path("buy-history/", BuyHistoryAPIView.as_view(), name="buy-history"),
    # path("contact/", ContactUsListAPIView.as_view(), name="contact"),
    path("dialog/", GetDialog.as_view(), name="dialog"),
]
