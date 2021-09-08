from django.db import models
from django.db.models.fields import DateField

import uuid

from django.utils.translation import gettext_lazy as _

from stdimage.models import StdImageField 

ICONE_CHOICES = (
        ('lni-laptop-phone', _('Notebook')),
        ('lni-cog', _('Engrenagem')),
        ('lni-leaf', _('Folha')),
        ('lni-layers', _('Design')),
        ('lni-mobile', _('Mobile')),
        ('lni-rocket', _('Foguete')),
        ('lni-users', _('Usuários')),
        ('lni-stats-up', _('Gráfico')), 
        ('lni-package',_('Pacote')), 
        ('lni-drop',_('Gota')),
        ('lni-star',_('Estrela'))
    ) 

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1] 
    filename = f'{uuid.uuid4()}.{ext}' 
    return filename

class Base(models.Model): 
    criado = models.DateField(_('Criação'),auto_now_add=True) 
    modificado = models.DateField(_('Atualização'),auto_now=True) 
    ativo = models.BooleanField(_('Ativo?'),default=True) 
    
    class Meta:
        abstract = True 

class Servico(Base):
    servico = models.CharField(_('Serviço'),max_length=100) 
    descricao = models.TextField(_('Descrição'),max_length=200) 
    icone = models.CharField(_('Icone'),max_length=16,choices=ICONE_CHOICES) 

    class Meta:
        verbose_name = _('Serviço') 
        verbose_name_plural = _('Serviços') 

    def __str__(self): 
        return self.servico 


class Feature(Base):
    feature = models.CharField(_('Features'),max_length=100)
    descricao = models.TextField(_('Descrição'),max_length=200)
    icone = models.CharField(_('Icone'),max_length=16,choices=ICONE_CHOICES) 
    
    class Meta: 
        verbose_name = _('Recurso') 
        verbose_name_plural = _('Recursos') 
    
    def __str__(self):
        return self.feature

class Cargo(Base): 
    cargo = models.CharField(_('Cargo'),max_length=100) 

    class Meta: 
        verbose_name = _('Cargo') 
        verbose_name_plural = _('Cargos') 

    def __str__(self): 
        return self.cargo 

class Funcionario(Base):
    nome = models.CharField(_('Nome'),max_length=100) 
    cargo = models.ForeignKey('core.Cargo',verbose_name=_('Cargo'),on_delete=models.CASCADE) 
    bio = models.TextField('BIO',max_length=300) 
    imagem = StdImageField(_('Imagem'),upload_to=get_file_path,variations={'thumb': {"width": 480, "height": 480, "crop":True}}) 
    facebook = models.CharField(_('Facebook'), max_length=100,default='#') 
    instagram = models.CharField(_('Instagram'), max_length=100,default='#') 
    twitter = models.CharField(_('Twitter'), max_length=100,default='#') 

    class Meta:
        verbose_name = _('Funcionário') 
        verbose_name_plural = _('Funcionários') 

    def __str__(self):
        return self.nome  

class Pacote(Base):
    pacote = models.CharField(_('Pacote'),max_length=100) 
    preco = models.DecimalField(_('Preço'),max_digits=5, decimal_places=2) 
    descricao = models.TextField(_('Descrição'),max_length=100) 
    icone = models.CharField(_('Icone'),max_length=16,choices=ICONE_CHOICES) 

    class Meta:
        verbose_name = _('Pacote')
        verbose_name_plural = _('Pacotes') 

    def __str__(self):
        return self.pacote 

class Cliente(Base): 
    SCORE_CHOICES = zip(range(1,6), range(1,6))
    nome = models.CharField(_('Nome'),max_length=100) 
    profissao = models.CharField(_('Profissão'),max_length=30) 
    avaliacao = models.TextField(_('BIO'),max_length=300) 
    imagem = StdImageField(_('Imagem'),upload_to=get_file_path,variations={'thumb': {"width": 75, "height": 75, "crop":True}}) 
    stars  = models.IntegerField(choices=SCORE_CHOICES, blank=False)
    class Meta:
        verbose_name = _('Cliente') 
        verbose_name_plural = _('Clientes') 

    def __str__(self):
        return self.nome
