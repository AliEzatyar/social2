from django import template
from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag(name="provider_login_url")
def provider_login(appname):
    return f"https://www.mysite.com:8080/accounts/{appname}/login/?process=login"

@register.filter(name="is_followers")
def followers(f_user,fd_user):
    user_followers = fd_user.followers_relations.all()
    print(user_followers,fd_user)
    try:
        if user_followers.values().get(From=f_user.id):
            print("it is")
            return True
    except:
        return False
