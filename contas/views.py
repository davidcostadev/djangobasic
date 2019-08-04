from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import TransaoFrom
from .models import Transacao
import datetime
# Create your views here.

def home(request): 
    data = {}
    data['transacoes'] = ['Transaçâo1', 'Transaçâo2', 'Transaçâo3']
    now = datetime.datetime.now()
    data['now'] = now.strftime("%H:%M:%S")
    #html = "<html><body> Agora são - %s</body></html>" % now
    return render(request, 'contas/home.html',data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

def nova_transcao(request):
    data = {}
    form = TransaoFrom(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    return render(request, 'contas/form.html', data)
