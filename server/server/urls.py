"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/news', include('news.api.urls')),
    url(r'^api/news',include(('news.api.urls','api-articles'),namespace='api-articles')),
    url(r'^api/news/?', include(('news.api.urls','article-detail'),namespace='article-detail'))
    # path('api/',include('news.api.urls')),
    # path('',RedirectView.as_view(url='api/',permanent=True)),
]
