from django.urls import path
from images.views import create_image,show_detail,like,show_images
# from .views import bookmarkit_js
app_name = "images"
urlpatterns = [
    path("create/", create_image, name="create"),
    path("detail/<int:id>/<slug:slug>",show_detail,name="detail"),
    path("like/",like,name="like"),
    path("",show_images,name="images_list"),
    # path("bookmarklet/", bookmarkit_js, name="bookmarkit_func")
]
