from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT)

from api.serializations import (BuySerializer, CarasolModelSerializer,
                                ContactUsSerializer, ItemsSerializer,
                                NewUserSerializer, PaymentMethodSerializer,
                                ServicesSerializer)
from landing.models import (Buy, CarasolModel, ContactUs, Items, NewUser,
                            PaymentMethod, Services)


class CarasolModelListAPIView(RetrieveAPIView):
    queryset = CarasolModel.objects.all()
    serializer_class = CarasolModelSerializer


class ServicesListAPIView(RetrieveAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ItemsListAPIView(RetrieveAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer


class PaymentMethodListAPIView(RetrieveAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer


class BuyListAPIView(RetrieveAPIView):
    queryset = Buy.objects.all()
    serializer_class = BuySerializer


class ContactUsListAPIView(RetrieveAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


# get the user buy history
class BuyHistoryAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BuySerializer

    def get_queryset(self):
        return Buy.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return Response(self.get_queryset().values())


# register the user
class RegisterAPIView(CreateAPIView):
    queryset = NewUser.objects.all()
    model = NewUser()
    serializer_class = NewUserSerializer
    # serializer_class = NewUserSerializer

    # def post(self, request, *args, **kwargs):
    #     # serializer = self.serializer_class(data=request.data)
    #     # check if user already exists
    #     if NewUser.objects.filter(email=request.data["email"]).exists():
    #         return Response({"error": "Email already exists"}, status=HTTP_409_CONFLICT)
    #     if NewUser.objects.filter(username=request.data["phone"]).exists():
    #         return Response(
    #             {"error": "Phone number already exists"}, status=HTTP_409_CONFLICT
    #         )
    #     # check if passwords match
    #     if request.data["password"] != request.data["password2"]:
    #         return Response(
    #             {"error": "Passwords don't match"}, status=HTTP_400_BAD_REQUEST
    #         )
    #     # create the user and save it to the database and return 201 status code
    #     user = NewUser.objects.create_user(
    #         username=request.data["phone"],
    #         email=request.data["email"],
    #         password=request.data["password"],
    #         # first name and last name are optional
    #         first_name=request.data.get("first_name", ""),
    #         last_name=request.data.get("last_name", ""),
    #     )
    #     user.save()
    #     return Response({"success": "User created"}, status=HTTP_201_CREATED)

    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data, status=HTTP_200_OK)

    # user = NewUser.objects.create_user(
    #     username=request.data["username"],
    #     phone=request.data["phone"],
    #     email=request.data["email"],
    #     password=request.data["password"],
    # )
    # user.save()
    # return Response({"message": "User created successfully"}, status=HTTP_200_OK)


# get the user profile
class ProfileAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = NewUserSerializer

    def get_queryset(self):
        return NewUser.objects.filter(id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return Response(self.get_queryset().values())


# update the user profile
class UpdateProfileAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = NewUserSerializer

    def get_queryset(self):
        return NewUser.objects.filter(id=self.request.user.id)

    def post(self, request, *args, **kwargs):
        user = NewUser.objects.get(id=self.request.user.id)
        user.username = request.data["username"]
        user.phone = request.data["phone"]
        user.email = request.data["email"]
        user.save()
        return Response({"message": "User updated successfully"}, status=HTTP_200_OK)


# logout the user
class LogoutAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = NewUserSerializer

    def get_queryset(self):
        return NewUser.objects.filter(id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({"message": "User logged out successfully"}, status=HTTP_200_OK)
