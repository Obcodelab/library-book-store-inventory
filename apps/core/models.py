import uuid
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )

    class Meta:
        abstract = True


class Book(BaseModel):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.CharField(max_length=100)
    publisher = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.title}"


class Inventory(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity_available = models.IntegerField(default=0)
    quantity_borrowed = models.IntegerField(default=0)
    quantity_purchased = models.IntegerField(default=0)

    def __str__(self):
        return f"Inventory for {self.book.title}"


class Customer(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Transaction(BaseModel):
    TRANSACTION_TYPES = [
        ("borrow", "Borrow"),
        ("purchase", "Purchase"),
        ("return", "Return"),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    transaction_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)  # For borrow transactions
    return_date = models.DateField(null=True, blank=True)  # For return transactions
    late_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.transaction_type} of {self.book.title} by {self.customer.first_name}"

    class Meta:
        ordering = ["-transaction_date"]


class Purchase(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    supplier_name = models.CharField(max_length=255)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_purchased = models.IntegerField()

    def __str__(self):
        return f"Purchase of {self.book.title} from {self.supplier_name}"


class Sale(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_sold = models.IntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale of {self.book.title} to {self.customer.first_name}"
