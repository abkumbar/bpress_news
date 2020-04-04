from rest_framework import serializers
from news.models import Article

class newsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'headline',
            'author',
            'date_published',
            'location',
            'description',
        )
