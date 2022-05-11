from django.contrib import admin
from django.urls import path

from Kitobxon.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('ustoz1/', Ustoz1),
    path('katta_muallif/', muallif),
    path('record/', record),
    path('ilmiy/', ilmiy),
    path('erkak/', erkak),
    path('kitoblar/', Kitoblar),
    path('mualliflar/', Mualliflar),
    path('recordlar/', records),
    path('kitoblar/<int:pk>/', kitob_ochir),
    path('muallif_edit/<int:son>/', edit_auth),
    path('edit_book/<int:son>/', edit_book),
]