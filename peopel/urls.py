from django.urls import path
from . import views
app_name = "people"
urlpatterns = [
    path("",views.people,name="people_view")

]