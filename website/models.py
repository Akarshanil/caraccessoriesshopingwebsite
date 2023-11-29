from django.db import models
from django.contrib.auth.models import User
from myapp.models import productsave


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(productsave, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price=models.IntegerField(null=True)
class delivaryuser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(productsave, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    mobilenumber = models.IntegerField()
    landmark = models.CharField(max_length=250)
    twon_or_city = models.CharField(max_length=250)
class contsave(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone=models.IntegerField()
    textarea=models.CharField(max_length=255)
class customerreview(models.Model):
    name=models.CharField(max_length=255)
    discription=models.CharField(max_length=255)

class codsave(models.Model):
    deluser = models.ForeignKey(delivaryuser,on_delete=models.CASCADE)
    mode_of_payment=models.CharField(max_length=100)
class razorpaydb(models.Model):
    deluserrazorpay = models.ForeignKey(delivaryuser,on_delete=models.CASCADE)
    mode_of_paymentrazorpay=models.CharField(max_length=100)
    paymentid=models.CharField(null=True,max_length=255)



