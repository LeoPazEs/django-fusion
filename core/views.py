from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from django.utils import translation
from django.utils.translation import gettext as _

from .models import Servico, Funcionario, Feature, Pacote,Cliente
from .forms import ContatoForm

class IndexView(FormView):
    template_name = 'index.html' 
    form_class = ContatoForm 
    success_url = reverse_lazy('index') 

    def get_context_data(self, **kwargs): 
        features_count = Feature.objects.count()/2 
        context = super(IndexView,self).get_context_data(**kwargs) #caso tenha mais dados vindo de algum lugar

        lang = translation.get_language()

        context['servicos'] = Servico.objects.order_by('?').all() 
        context['funcionarios'] = Funcionario.objects.order_by('?').all() 
        context['features_left'] = Feature.objects.all()[:features_count]
        context['features_right'] = Feature.objects.all()[features_count:]
        context['pacotes'] = Pacote.objects.order_by('preco').all() 
        context['clientes'] = Cliente.objects.order_by('?').all() 
        context['lang'] = lang
        translation.activate(lang)
        return context 
    
    def form_valid(self,form,*args,**kwargs):
        form.send_mail()
        messages.success(self.request,_('E-mail enviado com sucesso')) 
        return super(IndexView,self).form_valid(form,*args,**kwargs) 

    def form_invalid(self, form ,*args ,**kwargs): 
        messages.error(self.request,_('Erro ao enviar e-mail'))
        return super(IndexView,self).form_invalid(form,*args,**kwargs)

