from __future__ import unicode_literals

from django.shortcuts import render

import json
import urllib
import re

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    return HttpResponse("Oi, você chegou até a view!")


@csrf_exempt # isenta o sistema de csrf para o Django não achar que é ataque kkkk

@require_POST # Não sei pra que serve ainda

def webhook(request):

    # imprimir valores do body

    jsondata = request.body
    print(jsondata)
    body = json.loads(jsondata)
    
    # imprimir valores do header http

    regex = re.compile('^HTTP_')
    header = dict((regex.sub('', header), value) for (header, value) 
       in request.META.items() if header.startswith('HTTP_'))
    print(header)


    try:
        # exemplo do repositório do ONS
        # tenta baixar o arquivo a partir da url recebida
        #arquivo = urllib.urlretrieve(body['url'])
        pass
    except:
        print("Erro ao recuperar arquivo.")
        return HttpResponse("Erro ao recuperar arquivo",status=500)
    else:
        #abre o arquivo e trata o que fazer com ele
        #contents = open(arquivo[0]).read()
        print("Sinal Recebido com Sucesso")
    
    return HttpResponse("Ok",status=201)