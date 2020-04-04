from .views import newsAPIView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', newsAPIView.as_view(), name='article-create'),
]