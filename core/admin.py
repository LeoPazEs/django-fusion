from django.contrib import admin

from .models import Cargo,Pacote,Servico,Funcionario,Feature,Cliente

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin): 
    list_display = ('cargo','ativo','modificado') 

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin): 
    list_display = ('servico','descricao','icone','ativo','modificado') 

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin): 
    list_display = ('nome','cargo','ativo','modificado') 

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin): 
    list_display = ('feature','descricao','icone','ativo','modificado') 

@admin.register(Pacote)
class PacoteAdmin(admin.ModelAdmin):
    list_display = ('pacote','preco','descricao','icone','ativo','modificado') 

@admin.register(Cliente)
class Cliente(admin.ModelAdmin):
    list_display = ('nome','profissao','avaliacao','stars','imagem','ativo','modificado') 


