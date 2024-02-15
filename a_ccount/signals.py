import os

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.models import EmailAddress
from .models import Profile
import requests  # for downloading users profile photo
from io import BytesIO
from allauth.socialaccount.models import SocialAccount, SocialToken


def get_facebook_profile_photo(access_token):
    print("access token found", access_token)
    url = f"https://graph.facebook.com/v14.0/me/picture?type=large&access_token={access_token}"
    response = requests.get(url)

    profile_photo_file = BytesIO(response.content)
    print("photo was downloaded")
    return profile_photo_file


@receiver(post_save, sender=SocialAccount)
def create_profile(sender, instance, created, **kwargs):
    print(SocialToken.objects.all())
    print("created profile was called", sender, instance, created, kwargs)
    if created:  # if User object was created
        # print(SocialAccount.objects.all())
        # print(instance.socialaccount_set)
        # print(dir(instance))
        # print("social accounts in my project: ",SocialAccount.objects.all())
        # print(SocialAccount.objects.get(provider="facebook"))
        # print("instance social account set: ",instance.socialaccount_set)
        # social_account = instance.socialaccount_set.filter(provider='facebook').first()
        # print(social_account)
        # if social_account:
        #     print("social account_found:", social_account)
        print("social account was created:-------->", instance)
        social_token = SocialToken.objects.all()
        print(social_token)
        # print(instance.socialtoken_set)
        # social_token = instance.socialtoken_set
        # access_token = social_token.token
        # print("access token:--------->", access_token)
        #
        # profile_photo = get_facebook_profile_photo(access_token)

        # pr = Profile.objects.create(user=instance.user)
        # pr.images.save(f'{str(instance)}.jpg', profile_photo)
        # print("saved successfully")
    # else:
    #     pf = Profile.objects.create(user=instance.user)


#

@receiver(post_save, sender=EmailAddress)
def save_profile(sender, instance, **kwargs):
    print("save profile was called")
    instance.user.profile.save()
