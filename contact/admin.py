from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    # CAMPOS A SEREM MOSTRADOS PARA ORDENAÇÃO NO ADM
    list_display = (
        'id', 'first_name','last_name','phone', 'category',
    )
    
    # ORDENAÇÃO PADRÃO
    ordering = (
        '-id',
    )

    # FILTRO NA PARTE DIRETIRA DA TELA
    list_filter = (
        'created_date',
    )

    # CAMPO DE PESQUISA
    search_fields = (
        'id', 
        'first_name',
        'last_name',
    )

    # QUANTOS ITENS VAI SER EXIBIDO POR PÁGINA
    list_per_page = 10
    
    # MÁXIMO EXIBIDO QUANDO CLICAR EM 'VER TODOS'
    list_max_show_all = 50

    # CRIA UMA CAIXA DE TEXTO PARA EDITAR O CONTATO DIRETAMENTE NA PAGINA
    # list_editable = ('first_name', 'last_name',)

    # CRIA UM LINK PARA EDITAR O CONTATO
    list_display_links = (
        'id',
        #'first_name',
    )

@admin.register(models.Category)
class CaregoryAdmin(admin.ModelAdmin):
    # CAMPOS A SEREM MOSTRADOS PARA ORDENAÇÃO NO ADM
    list_display = (
        'name',
    )

    ordering = (
        '-id',
    )