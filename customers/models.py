from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class Customer(models.Model):
    created_at = models.DateTimeField('Created At', auto_now_add=True, editable=False)
    modified_at = models.DateTimeField('Modified At', auto_now=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='customer',
        verbose_name='User',
    )


class CustomerAudit(models.Model):
    timestamp = models.DateTimeField('Timestamp', auto_now_add=True, editable=False)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='audits',
        verbose_name='Customer',
    )
