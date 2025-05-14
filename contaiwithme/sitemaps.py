# contaiwithme/sitemaps.py
from django.contrib.sitemaps import Sitemap
from servicios.models import Servicio

class ServicioSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Servicio.objects.filter(estado='Activo')  # Opcional: solo servicios activos

    def lastmod(self, obj):
        return obj.updated_at
