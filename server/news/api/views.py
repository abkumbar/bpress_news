from rest_framework import generics, mixins
from news.models import Article
from .serializers import newsSerializer

class newsAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    resource_name = 'newsArticle'
    serializer_class = newsSerializer

    def get_queryset(self):
        return Article.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
