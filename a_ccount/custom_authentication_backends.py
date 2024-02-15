from django.contrib.auth.backends import BaseBackend

# from a_ccount.models import CustomUser


# class EmailBackend(BaseBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             user = CustomUser.objects.get(email=username)
#             if user.check_password(password):
#                 return user
#             else:
#                 return 'Invalid password'
#         except CustomUser.DoesNotExist:
#             return None
#
#     def get_user(self, user_id):
#        try:
#            return CustomUser.objects.get(pk=user_id)
#        except CustomUser.DoesNotExist:
#            return None
from django.contrib.auth.models import User


class EmailAuthentication:
    def authenticate(self, request, username=None, password=None):
        try:
            # print("auhtenticate of email is called: ", request, "\t", password, "\temail:", username)
            user = User.objects.get(email=username)
            # if user is not None:
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        try:
            # print("get user is called:", user_id)
            user = User.objects.get(pk=user_id)
            return user
        except User.DoesNotExist:
            return None


class LastNameAuthentication:
    """
        authentication of user against last name and password
    """

    def authenticate(self, request, username=None, password=None):
        # print("LastnameAuthentication authenticate method was called:", request, username, password)
        try:
            user = User.objects.get(last_name=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        print("get user mehtod of LastNameAuthenticaion was called:","user_id",user_id)
        try:
            user = User.objects.get(id=user_id)
            return user
        except User.DoesNotExist:
            return None
