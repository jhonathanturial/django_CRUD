from django import forms
from .models import Transacao


class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['data', 'descricao', 'valor', 'categoria', 'observacoes']