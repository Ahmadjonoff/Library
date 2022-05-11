from django.forms import ModelForm
from .models import *

class KitobForm(ModelForm):
    class Meta:
        model = Kitob
        fields = '__all__'

class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = '__all__'