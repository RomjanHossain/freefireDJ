from django.contrib.auth.models import AbstractUser, User
from django.db import models
from rest_framework.authtoken.models import Token


class NewUser(AbstractUser):
    phone = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Users"


# carasol model
class CarasolModel(models.Model):
    carasol_id = models.AutoField(primary_key=True)
    carasol_title = models.CharField(max_length=50, blank=True, null=True)
    carasol_description = models.CharField(max_length=200, null=True, blank=True)
    carasol_image = models.ImageField(upload_to="carasol/images")
    carasol_link = models.CharField(max_length=200)
    carasol_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.carasol_title

    class Meta:
        verbose_name_plural = "Slider"
        ordering = ["-carasol_title"]


class Services(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=50,
    )
    description = models.CharField(max_length=200, null=True, blank=True)
    poster = models.ImageField(upload_to="poster/images")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Services"
        ordering = ["-title"]


class Items(models.Model):
    PLAYER_TYPES = (
        ("player id", "player_id"),
        ("player_account", "player_account"),
    )
    id = models.AutoField(primary_key=True)
    price = models.IntegerField()
    # diamond = models.IntegerField()
    # diamond chartfield
    diamond = models.CharField(max_length=50)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    player_type = models.CharField(max_length=50, choices=PLAYER_TYPES, default="id")

    def display_service(self):
        # return self.service.title
        return "{} - {} - {}tk".format(self.service.title, self.diamond, self.price)

    def __str__(self):
        # return self.service.title
        return "{} - {} - {}tk".format(self.service.title, self.diamond, self.price)

    class Meta:
        verbose_name_plural = "Items"


class PaymentMethod(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="payment/images")
    account_id = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-name"]


# STATUS
STATUS_CHOICE = [
    ("Pending", "Pending"),
    ("Approved", "Approved"),
    ("Declined", "Declined"),
]


class Buy(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default="Pending")
    sender_number = models.CharField(max_length=50)
    trxId = models.CharField(max_length=50)
    player_id = models.CharField(max_length=50, blank=True, null=True, default="")
    player_account = models.CharField(max_length=50, blank=True, null=True, default="")
    player_password = models.CharField(max_length=50, blank=True, null=True, default="")

    def __str__(self):
        return "{}".format(self.item)

    class Meta:
        db_table = "Order"
        verbose_name_plural = "Orders"
        ordering = ["-date"]


# class ContactUs2(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     phone = models.CharField(max_length=50)
#     message = models.TextField()
#     youtube = models.CharField(max_length=200)
#     facebook = models.CharField(max_length=200)
#     twitter = models.CharField(max_length=200)
#     instagram = models.CharField(max_length=200)
#     last_modified = models.DateField(auto_now=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name_plural = "ContactUs"


# class ContactUs(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     phone = models.CharField(max_length=50)
#     message = models.TextField()
#     youtube = models.CharField(max_length=200)
#     facebook = models.CharField(max_length=200)
#     twitter = models.CharField(max_length=200)
#     instagram = models.CharField(max_length=200)
#     last_modified = models.DateField(auto_now=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name_plural = "ContactUs"

# dialog model
class Dialog(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title


# image field
class ImageModel(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="profile/")
    user = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # user = Token.objects.get(key=self.user)
        # return self.user.username
        return self.user

    class Meta:
        verbose_name_plural = "Profile Picture"
