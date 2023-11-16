from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

User = get_user_model()

AUDIT_ITEM_ACTION_CHOICES = (
    ('created', 'Created'),
    ('modified', 'Modified'),
    ('deleted', 'Deleted'),
)


class AuditItem(models.Model):
    timestamp = models.DateTimeField('Timestamp', auto_now_add=True, editable=False)
    # user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='User')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name='Content Type')
    object_id = models.CharField('Object ID', max_length=50)
    content_object = GenericForeignKey('content_type', 'object_id')
    action = models.CharField('Action', max_length=25, choices=AUDIT_ITEM_ACTION_CHOICES, default='created')

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]
