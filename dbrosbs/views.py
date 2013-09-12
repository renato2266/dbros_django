# Create your views here.

from django.http import HttpResponse
from models import *
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404


def hello_world(request):
  html = "<html><body><p>Hello, world!</p></body></html>"
  return HttpResponse(html)

#def index(request):
    #return render_to_response('index.html', )

def index(request):
    lista_nomi=Name.objects.all().order_by('cognome_nome').select_related('association')
    return render_to_response('index.html', {'lista_nomi':lista_nomi})


def scheda_soggetto(request, id):
	try:
		scheda_soggetto = Name.objects.select_related().get(pk=id)
		#query={'id__in':scheda_soggetto.association.pk}
		collegamenti = Area.objects.select_related('ambit').get(pk=scheda_soggetto.association.area_id)
		#return HttpResponse("'%s' nato a %s<br>" % (scheda_soggetto.cognome_nome,
		#scheda_soggetto.luogo_nascita))
		return render_to_response('scheda_soggetto.html', {'scheda_soggetto':scheda_soggetto, 'collegamenti':collegamenti})
	except Name.DoesNotExist:
		return HttpResponse("Codice %s inesistente" % id)

