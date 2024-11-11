from django.contrib import admin
from .models import TipoBodega, Bodega, Noticia, Like

@admin.register(TipoBodega)
class TipoBodegaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'metros_cuadrados', 'precio_mensual')

@admin.register(Bodega)
class BodegaAdmin(admin.ModelAdmin):
    list_display = ('codigo_unico', 'tipo', 'disponible')
    search_fields = ('codigo_unico', 'tipo__tipo')
    list_filter = ('disponible', 'tipo__tipo')

admin.site.register(Noticia)
admin.site.register(Like)