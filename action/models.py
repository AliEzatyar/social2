from argparse import Action

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.
from a_ccount.models import Relation


class Action(models.Model):
    f="ggggggggggggggggggggggg"
    f="iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
    user = models.ForeignKey('auth.User',
                             related_name='actions',
                             on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    target_ct = models.ForeignKey(ContentType,
                                  # limit_choices_to={'a_ccount.relation':Relation},
                                  blank=True,
                                  null=True,
                                  related_name='target_obj',
                                  on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField(null=True,
                                            blank=True)
    target_model_object = GenericForeignKey('target_ct', 'target_id')

    class Meta:

        indexes = [
            models.Index(fields=['-created']),
            models.Index(fields=['target_ct', 'target_id']),
        ]
    ordering = ['-created']
