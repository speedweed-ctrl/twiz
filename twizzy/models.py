from django.db import models
from django.contrib.auth.models import User

sizes=(
    ("XS","XS"),
    ("S","S"),
    ("M","M"),
    ("L","L"),
    ("XL","XL")
)

class product(models.Model):
    addedby=models.ForeignKey(to=User, on_delete=models.CASCADE)
    availableSizes=models.CharField(choices=sizes , max_length=3)
    currencyFormat=models.CharField(max_length=3,default='TND')
    currencyId=models.CharField(max_length=3,default='TND')
    description=models.TextField()
    installments=models.IntegerField()
    isFreeShipping=models.BooleanField(default=True)
    price=models.FloatField()
    title=models.CharField(max_length=100)
    image=models.ImageField()
    createdAt=models.DateField(auto_created=True)

    def __str__(self):
        return f'{self.title} size {self.availableSizes}'

    class Meta:
        ordering=['createdAt']


class order(models.Model):
    customer_name=models.CharField(max_length=150)
    customer_lastname=models.CharField(max_length=150)
    adrees_1=models.CharField(max_length=150)
    adrees_2=models.CharField(max_length=150)
    city=models.CharField(max_length=20)
    code_postal=models.IntegerField()
    phone_number=models.IntegerField()
    email=models.CharField(max_length=50)
    total=models.FloatField()
    isDeliverd=models.BooleanField(default=False)
    DeliverdAT=models.DateField()
    createdAt=models.DateField(auto_created=True)

    def __str__(self):
        return f'{self.customer_name} {self.customer_lastname} order { str(self.isDeliverd)}'

    class Meta:
        ordering=['createdAt']

class orderItem(models.Model):
    order=models.ForeignKey(to=order ,on_delete=models.CASCADE)
    size=models.CharField(choices=sizes, max_length=3)
    name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    price = models.FloatField()
    createdAt=models.DateField(auto_created=True)
    isFreeShiping=models.BooleanField()

    def __str__(self):
        return f'{str(self.quantity)} of {self.name}'

    class Meta:
        ordering=['createdAt']





