from django.forms import ModelForm
from .models import Transacao

class TransaoFrom(ModelForm):
    class Meta:
        model = Transacao
        fields = ['data', 'descricao', 'valor', 'categoria', 'observacoes']


