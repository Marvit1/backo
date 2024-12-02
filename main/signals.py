from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Reclam

@receiver(post_delete, sender=Reclam)
def adjust_reclam_indices(sender, instance, **kwargs):
    # Example: You could adjust the order of remaining instances here if needed
    # For instance, you might want to reassign order values
    # Reclam.objects.filter(order__gt=instance.order).update(order=F('order') - 1)
    pass
