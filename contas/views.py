from django.http import HttpResponse
from django.shortcuts import render
import datetime
from .models import Transacao
from .form import TransacaoForm
import logging

def horaAtual(request):
    now = datetime.datetime.now()
    return render(request, 'contas/home.html', {'atual': now})

def listagem(request):
    data = {}
    data["transacoes"] =["T1","T2","T3"]
    data["transacoes"] = Transacao.objects.all()
    return render(request, 'contas/listagem.html',{'data': data})



def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)
    logging.debug('Dados recebidos via POST: %s', request.POST)
    if form.is_valid():
        form.save()
        logging.info('Transacao salva com sucesso.')
        return listagem(request)
    else:
        for field, errors in form.errors.items():
            for error in errors:
                logging.error('Erro no campo %s: %s', field, error)
        # Adicione um registro de erro se o formulário for inválido
        logging.error('Formulário inválido: %s', form.errors)
    data["form"] = form
    return render(request, "contas/form.html", data)