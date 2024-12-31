from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from .models import Jewels

# Signal to check and delete the category if no jewels are associated with it after a jewel is deleted
@receiver(post_delete, sender=Jewels)
def delete_category_if_empty(sender, instance, **kwargs):
    category = instance.jewel_category
    if not category.jewels.exists():  # Check if there are no jewels in this category
        category.delete()

