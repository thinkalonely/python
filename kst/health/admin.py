from django.contrib import admin
from .models import Article, Industry

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'keywords', 'pub_date')

class IndustryAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'keywords', 'pub_date')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Industry, IndustryAdmin)
