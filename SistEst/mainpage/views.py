from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def contatos(request):
    #template = loader.get_template('contatos.html')
    #return HttpResponse(template.render())
    return render (request, 'contatos.html')