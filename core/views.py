from django.shortcuts import render
from .models import Area

def areas(request):
    # Todos as áreas
    all_a = Area.objects.all()
    
# Id da área Informática
    
    a_info = Area.objects.get(nome='Informática')
    # GET RETORNA UM DADO

# Áreas que começam com a letra 'E'
    
    area_e = Area.objects.filter(nome__startswith='E')
    # FILTER RETORNA UMA LISTA DE DADOS

# Áreas que terminam com as letras 'ica'
    area_ica = Area.objects.filter(nome__endswith='ica')

# Áreas que possuem o trecho 'mec'
    area_mec = Area.objects.filter(nome__contains='mec')

# Áreas que possuem o trecho 'mec' e iniciam com 'Ele (opcao1)
    area_mec_ele = Area.objects.filter(nome__contains='mec', nome__startswith='Ele')

# Áreas que possuem o trecho 'mec' e iniciam com 'Ele (opcao2)
    area_mec_ele2 = Area.objects.filter(nome__contains='mec').filter(nome__startswith='Ele')
    # MAIS RECOMENDADO
# Áreas que possuem id 1 ou id 3
    

#Áreas que possuem id 1 ou que termine com 'tos'


#Quantas areas terminam com as letras 'ica' (opcao1)


#Quantas areas terminam com as letras 'ica' (opcao2)


    #Imprimir cursos por ordem alfabética

    
    #Imprimir areas por ordem alfabética inversa

    

    contexto = {
         'all_a' : all_a,
         'a_info': a_info,
         'area_e' : area_e,
         'area_ica' : area_ica,
         'area_mec' : area_mec,
         'area_mec_ele' : area_mec_ele,
         'area_mec_ele2' : area_mec_ele2,

    }
    return render(request, 'areas.html', contexto)



def publicos(request):
    # Todos os públicos


    # Id do público 'Discentes'


    # Públicos que começam com a letra 'D'


    # Públicos que possuem o trecho 'centes


    # Públicos que possuem id 1 ou possuem o trecho 'terno'


    contexto = {

    }
    return render(request, 'publicos.html', contexto)



def cursos(request):
    # Listar todos os cursos


    # Listar cursos em ordem alfabética


    # Listar cursos em ordem alfabética inversa


    # Listar dados do curso de Android


    # Listar cursos com menos de 50 vagas


    # Listar cursos com mais de 50 vagas


    #Listar cursos que possuem vagas entre 35 e 70 vagas


    # Listar cursos que iniciam apenas em 2023


    # Listar cursos que iniciam no mês de dezembro de 2022


    # Listar cursos que são da área de Informática


    # Listar cursos que são da área de Eletromecânica


    # Listar cursos que são voltados para o público Docentes


    # Listar cursos que são voltados para o público Externo


    # Listar cursos que são voltados para o público Docentes e Discentes


    # Listar cursos que são voltados para o público Docentes ou Discentes


    # Listar cursos da área de Informática e que são voltados para o público Externo


    # Listar cursos da área de Informática, que são voltados para o público Discentes e que possuam mais de 40 vagas


    # Quantidade de cursos que são da área de Informática


    # Quantidade de cursos que são voltados para o público externo


    # Quantidade de cursos que são da área de Eventos e voltados para o público externo

    
    
    contexto = {
       
    }
    return render(request, 'cursos.html', contexto)