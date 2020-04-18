from rest_framework import serializers
from rest_framework.reverse import reverse
from news.models import Article

class newsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'type',
            'title',
            'headline',
            'author',
            'datePublished',
            'location',
            'body_text',
        )

# class newsSerializer(serializers.HyperlinkedModelSerializer):
#     # uri = reverse('article-detail')

#     class Meta:
#         model = Article
#         fields = [
#             'url',
#             'id',
#             'type',
#             'title',
#             'headline',
#             'author',
#             'datePublished',
#             'location',
#             'body_text',
#         ]
