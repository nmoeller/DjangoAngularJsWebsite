from django.contrib.sitemaps import Sitemap
from .models import Article

class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
       return Article.objects.all()
 
    def lastmod(self, item): 
       return item.updated_at
