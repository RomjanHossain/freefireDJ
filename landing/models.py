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
    carasol_title = models.CharField(max_length=50)
    carasol_description = models.CharField(max_length=200)
    carasol_image = models.ImageField(upload_to="carasol/images")
    carasol_link = models.CharField(max_length=200)
    carasol_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.carasol_title

    class Meta:
        ordering = ["-carasol_title"]


class Services(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    poster = models.ImageField(upload_to="poster/images")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Services"
        ordering = ["-title"]


class Items(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.IntegerField()
    diamond = models.IntegerField()
    service = models.ForeignKey(Services, on_delete=models.CASCADE)

    def display_service(self):
        return self.service.title

    def __str__(self):
        return str(self.id)

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

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "Buy"
        ordering = ["-date"]


class ContactUs(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    message = models.TextField()
    youtube = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "ContactUs"


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
