from django.contrib.auth import models as user_models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.conf import settings


#
#
# # Create your models here.
# class CustomUser(AbstractUser):
#     username = models.CharField(max_length=15,unique=True,primary_key=True)
#     email = models.EmailField()
#     password = models.CharField(max_length=18)
#     age = models.PositiveBigIntegerField(editable=False)

#
# class Have_Image_Manager(models.Manager):
#     def get_query_set(self):
#         return bookmarker.objects.exclude(image__isnull=True)
#
#
# class Actives(models.Manager):
#     def get_query_set(self):
#         return bookmarker.objects.filter(is_active=True)
#
#
# class bookmarker(user_models.AbstractUser):
#     # personal details
#     username = models.PositiveIntegerField(primary_key=True, unique=True)
#     password = models.CharField(max_length=20)
#     phone = models.PositiveIntegerField(unique=True)
#     first_name = models.PositiveIntegerField(null=True, blank=True)
#     last_name = models.PositiveIntegerField(null=True, blank=True)
#
#     # ohters
#     date_joined = models.DateField(auto_now_add=True)
#     images = models.ImageField(upload_to="bookmarkers\\templates", null=True, blank=True)
#     song = models.FileField(upload_to="bookmarkers\\songs", null=True, blank=True)
#
#     # state
#     is_active = models.BooleanField(default=False)
#
#     # managers
#     objects = models.Manager()
#     with_images = Have_Image_Manager()
#
#     class Meta:
#         ordering = ['-first_name']
#

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}."


class Relation(models.Model):
    From = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="following_relations")
    To = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="followers_relations")
    created = models.DateField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['-created'])
        ]
        ordering = ['-created']

    def __str__(self):
        return f"Follow relation from --{self.From}-- to --{self.To}--"

