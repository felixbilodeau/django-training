from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import CustomerAudit, Customer
from .signals import customer_created


@receiver(
    customer_created,
    sender=None,
    dispatch_uid='customers.receivers.customer_created',
)
def customer_created(sender, customer, *args, **kwargs):
    CustomerAudit.objects.create(
        customer=customer,
        action='created',
    )


@receiver(
    post_save,
    sender=Customer,
    dispatch_uid='customers.receivers.print_hello',
)
def print_hello(sender, instance, created, raw, *args, **kwargs):
    if raw:
        return
    
    if not created:
        print('Hello,', instance.user.first_name, instance.user.last_name)

    return
