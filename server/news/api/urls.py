from .views import newsAPIView, articleRudView
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    url(r'^$', newsAPIView.as_view(), name='article-create'),
    url(r'^(?P<id>\d+)$', articleRudView.as_view(), name='article-detail'),
    # path('news/', newsAPIView.as_view(),name='article-create'),
    # path('news/<int:pk>',articleRudView.as_view(), name='article-detail')
]