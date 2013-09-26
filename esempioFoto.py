VIEWS

@login_required
@user_passes_test(lambda u: u.profile.is_township())
def crea_blocco(request):
    cimiteri= Cimitero.objects.all()
    if request.method == "POST":
        form = NuovoBloccoForm(request.POST,request.FILES)
        if form.is_valid():
            cleanedData = form.cleaned_data
            blocco=Blocco()
            blocco.nome=cleanedData.get("nome")
            blocco.cimitero_id=cleanedData.get("cimitero")
            blocco.settore_id=cleanedData.get("settore")
            blocco.numfile=cleanedData.get("numFile")
            blocco.numverticale=cleanedData.get("numVerticale")
            latitudine=cleanedData.get("latitudine")
            longitudine=cleanedData.get("longitudine")
            totale=blocco.numfile*blocco.numverticale
            blocco.liberi=totale
            blocco.image=request.FILES.get('image')
            blocco.save()
            if cleanedData.get("check")=='noweb':
                stato='vuoto'
            else:
                stato='on-line'
            print stato
            idBlocco=Blocco.objects.latest('id')
            numLoc=0
            for i in range(1,cleanedData.get("numVerticale")+1):
                for j in range(1,cleanedData.get("numFile")+1):
                    numLoc=numLoc+1
                    loculo=Loculo()
                    loculo.nome= 'Loculo%s' %str(numLoc)
                    loculo.blocco_id=idBlocco.id
                    loculo.fila=j
                    loculo.verticale=i
                    loculo.stato=stato
                    loculo.concessionario_id=0
                    loculo.quantita=0
                    loculo.luce='spento'
                    loculo.latitudine=latitudine
                    loculo.longitudine=longitudine
                    loculo.save()

            form = NuovoBloccoForm(initial={'latitudine':'0,0','longitudine':'0,0'})
            variables = {"title":"Nuove aree","label":"Inserimento effettuato","cimiteri":cimiteri,"form":form}
            return render_to_response("crea_blocco.html",RequestContext(request,variables))
    else:
        form = NuovoBloccoForm(initial={'latitudine':'0,0','longitudine':'0,0'})
    
    variables = {"title":"Nuove aree","cimiteri":cimiteri,"form":form}
    return render_to_response("crea_blocco.html",RequestContext(request,variables))
    
    
FORMS

class NuovoBloccoForm(forms.Form):
    CHOICES = (('noweb','Concessione Manuale'),('web','Concessione Web'))
    cimitero = forms.CharField(label=u'Cimitero', required=True)
    settore = forms.CharField(label=u'Settore', required=True)
    nome = forms.CharField(label=u'Nome', required=True)
    numFile = forms.IntegerField(label=u'Numero file', required=True)
    numVerticale = forms.IntegerField(label=u'Numero colonne', required=True)
    latitudine = forms.CharField(label=u'Latitudine', required=True)
    longitudine = forms.CharField(label=u'Longitudine', required=True)
    check = forms.ChoiceField(choices=CHOICES)
    image = forms.ImageField(required=False)
    
    
MODELS

class Blocco(models.Model):
	nome=models.CharField(max_length=255)
	cimitero=models.ForeignKey(Cimitero)
	settore=models.ForeignKey(Settore)
	numfile=models.IntegerField()
	numverticale=models.IntegerField()
	liberi=models.IntegerField()
	image=models.ImageField(upload_to='mappe', blank = True, null=True)
	
	
TEMPLATE

<form method="POST" action="" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.non_field_errors }}
    <table>
        <tr>
            <td>Cimitero:</td>
            <td>
              <select name="cimitero" id="id_cimiteri" onchange="Dajaxice.cimiteroapp.fill_topo_combo(Dajax.process,{'tipo': 'cimitero', 'option':(this.value)})">
                <option value="0">Selezionare il cimitero</option>
                {% for item in cimiteri %}
                    <option value="{{ item.id }}">{{ item.nome }}</option>
                {% endfor %}
              </select>
            </td>
        </tr>
        <tr>
            <td>Settore:</td>
            <td>
              <select name="settore" id="id_settori">
                  <option value="0">Selezionare il settore </option>
               </select> 
            </td>
        </tr>
        <tr><td>{{form.nome.label}}:</td><td>{{form.nome.errors}} {{form.nome}}</td></tr>

        <tr>
            <td>{{form.numFile.label}}:</td>
            <td>{{form.numFile.errors}} {{form.numFile}}</td>
        </tr>
        <tr>
            <td>{{form.numVerticale.label}}:</td>
            <td>{{form.numVerticale.errors}} {{form.numVerticale}}</td>
        </tr>
        <tr>
            <td>{{form.latitudine.label}}:</td>
            <td>{{form.latitudine.errors}} {{form.latitudine}}</td>
        </tr>
        <tr>
            <td>{{form.longitudine.label}}:</td>
            <td>{{form.longitudine.errors}} {{form.longitudine}}</td>

        </tr>
        <tr>
            <td>{{form.check.label}}:</td>
            <td>{{form.check}}</td>
        </tr>
        <tr>
            <td>Immagine:</td>
            <td>{{form.image}}</td>
        </tr>
    </table>
    <br />
    <input type="submit" value="Salva"/>
</form>
