from rest_framework.serializers import ModelSerializer

from landing.models import (Buy, CarasolModel, ContactUs, Items, NewUser,
                            PaymentMethod, Services)


class CarasolModelSerializer(ModelSerializer):
    class Meta:
        model = CarasolModel
        fields = "__all__"


class ServicesSerializer(ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"


class ItemsSerializer(ModelSerializer):
    class Meta:
        model = Items
        fields = "__all__"


class PaymentMethodSerializer(ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = "__all__"


class BuySerializer(ModelSerializer):
    class Meta:
        model = Buy
        fields = "__all__"


class ContactUsSerializer(ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"


class NewUserSerializer(ModelSerializer):
    def create(self, validated_data):
        # cleaned the data
        cleaned_data = self.validate(validated_data)
        # create the user
        user = NewUser.objects.create_user(
            username=cleaned_data["username"],
            email=cleaned_data["email"],
            password=cleaned_data["password"],
            phone=cleaned_data["phone"],
            first_name=cleaned_data["first_name"],
            last_name=cleaned_data["last_name"],
        )

        # user = NewUser.objects.create_user(**validated_data)
        # user = NewUser.objects.create_user(
        #     username=validated_data["username"],
        #     phone=validated_data["phone"],
        #     email=validated_data["email"],
        #     password=validated_data["password"],
        #     first_name=validated_data.get("first_name", ""),
        #     last_name=validated_data.get("last_name", ""),
        # )
        user.set_password(validated_data["password"])
        user.save()
        return user

    def validate(self, data):
        if NewUser.objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError("Email already exists")
        if NewUser.objects.filter(username=data["phone"]).exists():
            raise serializers.ValidationError("Phone already exists")
        if len(data["password"]) < 6:
            raise serializers.ValidationError("Password too short")
        if NewUser.objects.filter(username=data["username"]).exists():
            raise serializers.ValidationError("Username already exists")
        return data

    class Meta:
        model = NewUser
        # fields = "__all__"
        fields = ("email", "password", "first_name", "last_name", "phone", "username")
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            "phone": {"required": True},
            "email": {"required": True},
        }
