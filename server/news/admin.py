from django.contrib import admin
from .models import Article

@admin.register(Article)

class newsAdmin(admin.ModelAdmin):
    list_display = ['title', 'headline', 'author', 'datePublished', 'location', 'body_text','type']
