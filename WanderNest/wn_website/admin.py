from django.contrib import admin

from wn_website.models import Transport, Tour


# Register your models here.
@admin.register(Transport)
class Transport(admin.ModelAdmin):
    list_display = ['id','name','description']
    list_display_links = ['name']
    ordering = ['id','name']
    list_per_page = 15

@admin.register(Tour)
class Tour(admin.ModelAdmin):
    list_display = ['id','title','img_url','description','start_date','end_date','price','transport','creation_tour_date','slug']
    list_display_links = ['id','title']
    list_per_page = 10
    list_filter = ['transport','price','start_date','end_date']
