from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver

from .models import AuditItem
from .signals import model_saved

"""
explaination of args and kwargs

function(instance, user, action, commit=True)

[instance, user, action], {'commit': True}

*[instance, user, action] -> instance, user, action

**{'commit': True} -> commit=True

function(*args, **kwargs)

kwargs.get('commit')
"""


@receiver(model_saved, sender=None, dispatch_uid='audit.receviers.on_model_saved')
def on_model_saved(sender, instance, action, **kwargs):
    content_type = ContentType.objects.get_for_model(sender)
    object_id = instance.pk
    AuditItem.objects.create(
        # user=user,
        content_type=content_type,
        object_id=object_id,
        action=action,
    )
    print('Audit saved!')
