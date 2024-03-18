from django.core.signals import setting_changed
from django.dispatch import receiver


@receiver(setting_changed,)
def receiverr(sender,**kwargs):
    print(sender,"settings changed-------------------------")