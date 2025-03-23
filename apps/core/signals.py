from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta
from .models import Inventory, Transaction, Sale


@receiver(post_save, sender=Transaction)
def update_inventory_on_transaction(sender, instance, created, **kwargs):
    if created:
        inventory = Inventory.objects.get(book=instance.book)

        if instance.transaction_type == "borrow":
            if instance.due_date is None:
                instance.due_date = instance.transaction_date + timedelta(days=14)
                instance.save()
            inventory.quantity_available -= 1
            inventory.quantity_borrowed += 1
            inventory.save()

        elif instance.transaction_type == "return":
            inventory.quantity_available += 1
            inventory.quantity_borrowed -= 1
            inventory.save()

            if instance.return_date and instance.due_date:
                late_days = (instance.return_date - instance.due_date).days
                if late_days > 0:
                    instance.late_fee = late_days * 1.5
                    instance.save()

        elif instance.transaction_type == "purchase":
            inventory.quantity_available += 1
            inventory.quantity_purchased += 1
            inventory.save()


@receiver(post_save, sender=Sale)
def update_inventory_on_sale(sender, instance, created, **kwargs):
    if created:
        inventory = Inventory.objects.get(book=instance.book)
        inventory.quantity_available -= instance.quantity_sold
        inventory.save()
