from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from action.models import Action
import datetime as dt
from django.utils import timezone as tz
def create_action(user,verb,target_model_object=None):
    now = dt.datetime.now()
    _60s_ago = now - dt.timedelta(seconds=60)
    similars = Action.objects.filter(created__gte=_60s_ago,verb=verb,user=user)

    if target_model_object:
        target_content_type = ContentType.objects.get_for_model(target_model_object) #?
        similars.filter(target_ct=target_content_type,target_id=target_model_object.id)
    if not similars:
        # if there are no similar actions in previus 60 seconds
        action = Action.objects.create(verb=verb,user=user,target_model_object=target_model_object)
        action.save()
        return True
    return False

