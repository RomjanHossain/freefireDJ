from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveAPIView, UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT)

from api.serializations import (BuySerializer, CarasolModelSerializer,
                                ContactUsSerializer, ItemsSerializer,
                                NewUserSerializer, PaymentMethodSerializer,
                                ServicesSerializer, UpdateUserSerializer)
from landing.models import (Buy, CarasolModel, ContactUs, Items, NewUser,
                            PaymentMethod, Services)


class CarasolModelListAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CarasolModel.objects.all()
    serializer_class = CarasolModelSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class ServicesListAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class ItemsListAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class PaymentMethodListAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class BuyListAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    # queryset = Buy.objects.all()
    serializer_class = BuySerializer

    def get_queryset(self):
        user = self.request.user
        return Buy.objects.filter(user=user)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class ContactUsListAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


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


# get the user profile
class ProfileAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = NewUserSerializer

    def get_queryset(self):
        return NewUser.objects.filter(id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return Response(self.get_queryset().values())


# update the user profile
class UpdateProfileAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer

    def get_queryset(self):
        return NewUser.objects.filter(id=self.request.user.id)

    def put(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(
            queryset, data=request.data, partial=True, many=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


# logout the user
class LogoutAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = NewUserSerializer

    def get_queryset(self):
        return NewUser.objects.filter(id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({"message": "User logged out successfully"}, status=HTTP_200_OK)
