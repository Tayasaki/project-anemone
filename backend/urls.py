"""djangoHeroku URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest_framework import routers

from .api.views import *

router = routers.DefaultRouter()
router.register('users', UserViewSet)

router.register('event', EventViewSet)
router.register('eventRegistration', EventRegistrationViewSet)

router.register('location', LocationViewSet)
router.register('locationComment', LocationCommentViewSet)
router.register('locationRating', LocationRatingViewSet)

urlpatterns = [
    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    path('api/explorer/', include('rest_framework.urls', namespace='rest_framework')),

    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),

]
