"""
URL configuration for SocialWebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from a_ccount.views import dashboard_view

urlpatterns = [
    path('', dashboard_view),
    path('a_ccount/', include('a_ccount.urls', namespace='a_ccount')),
    path('admin/', admin.site.urls),
    # path('social-auth/', include("oauth2_provider.urls", namespace="social")),
    path("accounts/", include("allauth.urls")),
    path("images/", include("images.urls", namespace="images")),
    path("people/", include("peopel.urls", namespace="peopel"))
]
if settings.DEBUG:  # if we have set DEBUG==True
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
