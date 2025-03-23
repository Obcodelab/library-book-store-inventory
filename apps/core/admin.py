from django.contrib import admin
from .models import Book, Inventory, Customer, Transaction, Purchase, Sale


class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "isbn",
        "price",
    )
    search_fields = ("title", "isbn")  # Enable searching by title and isbn


class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "book",
        "quantity_available",
        "quantity_borrowed",
        "quantity_purchased",
    )


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email")


class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "book", "transaction_type", "transaction_date")
    search_fields = ("customer__first_name", "book__title")


class PurchaseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "book",
        "supplier_name",
        "purchase_price",
        "quantity_purchased",
    )


class SaleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "book",
        "quantity_sold",
        "sale_price",
        "sale_date",
    )


# Register models with custom admin views
admin.site.register(Book, BookAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Sale, SaleAdmin)
