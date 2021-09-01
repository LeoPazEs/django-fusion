from django.db import models
from django.db.models.fields import DateField

import uuid

from stdimage.models import StdImageField 

ICONE_CHOICES = (
        ('lni-laptop-phone', 'Notebook'),
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
        ('lni-users', 'Usuários'),
        ('lni-stats-up', 'Gráfico'), 
        ('lni-package','Pacote'), 
        ('lni-drop','Gota'),
        ('lni-star','Estrela')
    ) 

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1] 
    filename = f'{uuid.uuid4()}.{ext}' 
    return filename

class Base(models.Model): 
    criado = models.DateField('Criação',auto_now_add=True) 
    modificado = models.DateField('Atualização',auto_now=True) 
    ativo = models.BooleanField('Ativo?',default=True) 
    
    class Meta:
        abstract = True 

class Servico(Base):
    servico = models.CharField('Serviço',max_length=100) 
    descricao = models.TextField('Descrição',max_length=200) 
    icone = models.CharField('Icone',max_length=16,choices=ICONE_CHOICES) 

    class Meta:
        verbose_name = 'Serviço' 
        verbose_name_plural = 'Serviços' 

    def __str__(self): 
        return self.servico 


class Feature(Base):
    feature = models.CharField('Features',max_length=100)
    descricao = models.TextField('Descrição',max_length=200)
    icone = models.CharField('Icone',max_length=16,choices=ICONE_CHOICES) 
    
    class Meta: 
        verbose_name = 'Recurso' 
        verbose_name_plural = 'Recursos' 
    
    def __str__(self):
        return self.feature

class Cargo(Base): 
    cargo = models.CharField('Cargo',max_length=100) 

    class Meta: 
        verbose_name = 'Cargo' 
        verbose_name_plural = 'Cargos' 

    def __str__(self): 
        return self.cargo 

class Funcionario(Base):
    nome = models.CharField('Nome',max_length=100) 
    cargo = models.ForeignKey('core.Cargo',verbose_name='Cargo',on_delete=models.CASCADE) 
    bio = models.TextField('BIO',max_length=300) 
    imagem = StdImageField('Imagem',upload_to=get_file_path,variations={'thumb': {"width": 480, "height": 480, "crop":True}}) 
    facebook = models.CharField('Facebook', max_length=100,default='#') 
    instagram = models.CharField('Instagram', max_length=100,default='#') 
    twitter = models.CharField('Twitter', max_length=100,default='#') 

    class Meta:
        verbose_name = 'Funcionário' 
        verbose_name_plural = 'Funcionários' 

    def __str__(self):
        return self.nome  

class Pacote(Base):
    pacote = models.CharField('Pacote',max_length=100) 
    preco = models.DecimalField('Preço',max_digits=5, decimal_places=2) 
    descricao = models.TextField('Descrição',max_length=100) 
    icone = models.CharField('Icone',max_length=16,choices=ICONE_CHOICES) 

    class Meta:
        verbose_name = 'Pacote' 

    def __str__(self):
        return self.pacote 

class Cliente(Base): 
    SCORE_CHOICES = zip(range(1,6), range(1,6))
    nome = models.CharField('Nome',max_length=100) 
    profissao = models.CharField('Profissão',max_length=30) 
    avaliacao = models.TextField('BIO',max_length=300) 
    imagem = StdImageField('Imagem',upload_to=get_file_path,variations={'thumb': {"width": 75, "height": 75, "crop":True}}) 
    stars  = models.IntegerField(choices=SCORE_CHOICES, blank=False)
    class Meta:
        verbose_name = 'Cliente' 

    def __str__(self):
        return self.nome





