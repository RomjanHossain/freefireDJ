from django.contrib.auth import update_session_auth_hash
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveAPIView, RetrieveUpdateAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST,
                                   HTTP_404_NOT_FOUND,
                                   HTTP_405_METHOD_NOT_ALLOWED,
                                   HTTP_409_CONFLICT)

from api.serializations import (BuySerializer, CarasolModelSerializer,
                                ChangePasswordSerializer, ContactUsSerializer,
                                ImageSerializer, ItemsSerializer,
                                NewUserSerializer, PaymentMethodSerializer,
                                ServicesSerializer, UpdateUserSerializer)
from landing.models import (Buy, CarasolModel, ContactUs, ImageModel, Items,
                            NewUser, PaymentMethod, Services)


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
    # queryset = Items.objects.all()
    serializer_class = ItemsSerializer

    def get_queryset(self):
        queryset = Items.objects.filter(service_id=self.kwargs["pk"])
        return queryset

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
        return Response(self.get_queryset().values()[0])


# update the user profile
class UpdateProfileAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer

    def get_queryset(self):
        return NewUser.objects.filter(id=self.request.user.id)

    def get_object(self):
        pk = self.kwargs["pk"]
        queryset = self.get_queryset()
        obj = queryset.get(pk=pk)
        return obj

    def put(self, request, *args, **kwargs):
        # queryset = self.get_queryset().first()
        queryset = self.get_object()
        serializer = self.get_serializer(
            queryset,
            data=request.data,
            partial=True,
        )
        # serializer = self.get_serializer(
        #     queryset, data=request.data, partial=True, many=True
        # )
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


# change password
# class ChangePasswordAPIView(UpdateAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = ChangePasswordSerializer

#     def get_queryset(self):
#         return NewUser.objects.filter(id=self.request.user.id)

#     def get_object(self):
#         pk = self.kwargs["pk"]
#         queryset = self.get_queryset()
#         obj = queryset.get(pk=pk)
#         return obj

#     def put(self, request, *args, **kwargs):
#         queryset = self.get_object()
#         serializer = self.get_serializer(
#             queryset,
#             data=request.data,
#             partial=True,
#         )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=HTTP_200_OK)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  # noqa


class ChangePasswordView(UpdateAPIView):
    model = NewUser
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=HTTP_400_BAD_REQUEST,
                )
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            update_session_auth_hash(request, self.object)
            return Response("Success.", status=HTTP_200_OK)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


# get image detail
@api_view(["GET"])
def image_detail(request):
    try:
        # image = ImageModel.objects.get(pk=pk)
        # get image using user
        _image = ImageModel.objects.filter(user=request.auth.key)
    except ImageModel.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ImageSerializer(_image, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


# upload image
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def image_upload(request):
    # only allow authenticated users to upload images

    if request.method == "POST":
        _user = request.user
        _image = request.FILES.get("image")
        serializer = ImageSerializer(data={"user": _user, "image": _image})
        print("this is image -> ", _image)
        print("this is user -> ", _user)
        # serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    # get method is not allowed
    return Response(status=HTTP_405_METHOD_NOT_ALLOWED)


# convert that image_upload function into a class based view
class ImageUploadView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        # get user field data
        _user = request.data.get("user")
        _image = request.FILES.get("image")
        print("this is image -> ", _image)
        print("this is user -> ", _user)
        serializer = self.get_serializer(data={"user": _user, "image": _image})
        if serializer.is_valid():
            # check if user has already uploaded an image
            if ImageModel.objects.filter(user=_user).exists():
                # delete the previous image
                ImageModel.objects.filter(user=_user).delete()
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


# upload the user profile picture and get the user profile picture
class ProfilePictureAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ImageSerializer
    model = ImageModel()

    def get_queryset(self):
        return ImageModel.objects.filter(user=self.request.user)

    # def get_queryset(self):
    #     return NewUser.objects.filter(id=self.request.user.id)

    def get_object(self):
        pk = self.kwargs["pk"]
        queryset = self.get_queryset()
        obj = queryset.get(pk=pk)
        return obj

    def get(self, request, *args, **kwargs):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data, status=HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        queryset = self.get_object()
        serializer = self.get_serializer(
            queryset,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        queryset = self.get_object()
        queryset.profile_picture.delete()
        return Response(status=HTTP_204_NO_CONTENT)
