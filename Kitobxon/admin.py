from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Kitob, Muallif, Record

@admin.register(Kitob)
class KitobAdmin(ModelAdmin):
    search_fields = ['nomi', 'id']
    list_filter = ['janr']

@admin.register(Muallif)
class MuallifAdmin(ModelAdmin):
    search_fields = ['ismi', 'id']
    list_display = ['id', 'ismi', 'familiyasi', 'asarlar_soni']