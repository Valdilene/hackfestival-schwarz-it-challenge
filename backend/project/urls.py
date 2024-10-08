"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from upCycleRequest.views import UpCycleRequestListCreateView, UpCycleRequestRetrieveUpdateDeleteView
from item.views import ListCreateItemView, RetrieveUpdateDeleteItemView
from user.views import ListCreateStoreView, RetrieveUpdateDestroyStoreView

urlpatterns = [
    path('backend/admin/', admin.site.urls),
    path('backend/api/request/', UpCycleRequestListCreateView.as_view(), name='createRequest'),
    path('backend/api/request/<int:id>', UpCycleRequestRetrieveUpdateDeleteView.as_view(), name='createRequest'),
    path('backend/api/items/', ListCreateItemView.as_view(), name='items'),
    path('backend/api/items/<int:id>', RetrieveUpdateDeleteItemView.as_view(), name='items'),
    path('backend/api/store/', ListCreateStoreView.as_view(), name='store'),
    path('backend/api/store/<int:id>', RetrieveUpdateDestroyStoreView.as_view(), name='store'),
]
