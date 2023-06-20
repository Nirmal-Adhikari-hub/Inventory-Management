from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model): # class 'Category' will be the child calss of parent class 'models.Model'
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name # when you write 'str(Category(name="Shirts"))' then output = 'Shirts'. 
        #Basically, when you pass a new object of class Category to the str() function's argument, 
        # then the name attribute of the object will be returned as output.


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    # By default, the 'category' field in the Product model will point to the primary key '(id)' 
    # column of the Category model and same case with the 'supplier' field, unless you explicitly 
    # define 'to_feild' parameter.
    def __str__(self):
        return self.name


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('in', 'Incoming'),
        ('out', 'Outgoing'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(default=timezone.now)
    quantity = models.PositiveIntegerField()
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)

    def __str__(self):
        return f"{self.product} -> {self.quantity} units"