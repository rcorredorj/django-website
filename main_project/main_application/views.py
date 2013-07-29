# Create your views here.
from main_application.models import Article
from main_application.forms import ContactForm, ArticleForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
#from django.core.mail import EmailMessage
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

import logging
logger = logging.getLogger('logger')

@login_required(login_url='/home')
def about(request):
	html = "<html><body>Example</body></html>"
	return HttpResponse(html)

@login_required(login_url='/home')
def detail_article(request, id_article):
    data = get_object_or_404(Article, pk=id_article)
    return render_to_response('article.html',{'article':data}, context_instance=RequestContext(request))

@login_required(login_url='/home')
def contact(request):
    if request.method=='POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            titulo = 'Mensaje desde el recetario de Maestros del Web'
            contenido = contact_form.cleaned_data['message'] + "\n"
            contenido += 'Comunicarse a: ' + contact_form.cleaned_data['email']
            correo = EmailMessage(titulo, contenido, to=['destinatario@email.com'])
            correo.send()
            return HttpResponseRedirect('/')
    else:
        contact_form = ContactForm()
    return render_to_response('contactform.html',{'contact_form':contact_form}, context_instance=RequestContext(request))

@login_required(login_url='/home')
def new_article(request):
    if request.method=='POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid:
            article_form.save()
            return HttpResponseRedirect('/')
    else:
        article_form = ArticleForm()
    return render_to_response('articleform.html',{'article_form':article_form}, context_instance=RequestContext(request))

def home(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/private')
    if request.method == 'POST':
        # form sent
        authentication_form = AuthenticationForm(data=request.POST)        
        logger.error('RAC is_valid:'+str(authentication_form.is_valid()))
		
        if authentication_form.is_valid():
            #form OK
            usernm = request.POST['username']
            passwd = request.POST['password']
            access = authenticate(username=usernm, password=passwd)
            logger.error('user:'+usernm)
            if access is not None:
                if access.is_active:
                    login(request, access)
                    return HttpResponseRedirect('/private')
                #else:
                    #raise forms.ValidationError(_("This account is not active."))
                    #return render_to_response('noactivo.html', context_instance=RequestContext(request))
            #else:
                #raise forms.ValidationError(_("This user does not exist."))
                #return render_to_response('nousuario.html', context_instance=RequestContext(request))
    else:
        authentication_form = AuthenticationForm()
    return render_to_response('home.html',{'authentication_form':authentication_form}, context_instance=RequestContext(request))

@login_required(login_url='/home')
def private(request):
    usr = request.user
    articles = Article.objects.all()
    return render_to_response('private.html', {'usr':usr,'articles':articles}, context_instance=RequestContext(request))

@login_required(login_url='/home')
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/home')

