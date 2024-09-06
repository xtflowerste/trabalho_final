#importa duas bibliotecas.
import pandas as pd
import matplotlib.pyplot as plt

#lista com o nome de 10 alunos.
nomes_alunos = [
    "Alice", "Bob", "Carlos", "Diana", "Eduardo",
    "Fernanda", "Gabriel", "Helena", "Igor", "Juliana"
]

#um dicionário chamado notas_materias,
# Cada índice nas listas corresponde ao mesmo aluno da lista nomes_alunos.
notas_materias = {
    "matemática": [8.5, 7.0, 9.2, 6.8, 5.4, 7.6, 8.3, 9.1, 6.5, 7.9],
    "português": [7.2, 6.5, 8.0, 5.9, 6.8, 7.7, 8.1, 6.4, 7.3, 6.9],
    "história": [6.8, 7.4, 5.6, 8.2, 7.9, 6.3, 8.5, 7.1, 6.7, 5.8],
    "geografia": [8.3, 7.8, 6.5, 8.9, 7.4, 8.0, 7.2, 6.9, 8.1, 7.6],
    "ciências": [5.9, 6.8, 7.3, 6.1, 7.0, 5.6, 6.9, 7.4, 6.2, 5.8]
}

#média de cada matéria.
#definindo a função chamada calculador_media que recebe uma lista de notas como entrada.
def calculador_media(notas):
    return sum(notas) / len(notas)

#definindo a função chamada calcular_ira, que recebe dois parâmetros: notas_materias e nomes.
def calcular_ira(nomes, notas_materias):
    ira = {}
    #iniciamos um dicionário vazio.
    numero_materias = len(notas_materias)
    #len calcula o número total de matérias (número de chaves no dicionário notas_materias) 
    # e armazena o valor na variável numero_materias.
    for nome in nomes:
        ira[nome] = 0
#para cada 'nome' na lista 'nomes', o valor inicial do ira será 0.
    for materias, notas in notas_materias.items(): #items está retornando pares de chave e valor
        for nome, nota in zip(nomes, notas): #zip esta ligando nome com notas respectivamente.
            #somando todas as notas de cada aluno.
            ira[nome] += nota
    for nome in ira:
        ira[nome] = ira[nome] / numero_materias
    #para cada aluno a soma das notas é dividida pelo número de matérias.  
    return ira #retorna o valor da média de cada aluno p/ o dicionário ira.

#função para imprimir as notas de uma matéria específica.
def imprimir_notas_materia(materia): 
    #verifica se a matéria especificada está no dicionário 'notas_materias'.
    if materia in notas_materias: 
        #se a matéria existe, imprime o nome da matéria.
        print(f"Notas de {materia}:")
        #para cada aluno e sua respectiva nota na matéria, imprime o nome do aluno e a nota.
        for nome, nota in zip(nomes_alunos, notas_materias[materia]):
            print(f"{nome}: {nota}")
    else:
        #se a matéria não for encontrada, exibe uma mensagem de erro.
        print("Matéria não encontrada.")

#função para calcular e exibir a média de todas as matérias.
def imprimir_media_materias():
    medias = {} #dicionário para armazenar a média de cada matéria.
   
   #calcula a média de cada matéria e armazena no dicionário 'medias'.
    for materia, notas in notas_materias.items():
        medias[materia] = calculador_media(notas)

   #ordena as matérias pela média, do maior para o menor.
    medias_ordenadas = dict(sorted(medias.items(), key=lambda item: item[1], reverse=True))

    #cria e exibe um gráfico de barras com as médias das matérias.
    plt.bar(medias_ordenadas.keys(), medias_ordenadas.values(), color='blue') #color: define  cor do gráfico.
    #key: obtém as chaves do dicionário. values: obtém os valores do dicionário.
    plt.title("Média das Matérias")
    plt.xlabel("Matéria") #rótulo do eixo X.
    plt.ylabel("Média")  #rótulo do eixo Y.
    plt.show() #exibe o gráfico.

#função para calcular e exibir o IRA (Índice de Rendimento Acadêmico) dos alunos.
def imprimir_ira():
    ira = calcular_ira(nomes_alunos, notas_materias) #calcula o IRA dos alunos.
   
    #ordena os alunos pelo IRA, do maior para o menor.
    ira_ordenado = dict(sorted(ira.items(), key=lambda item: item[1], reverse=True))
   
    plt.bar(ira_ordenado.keys(), ira_ordenado.values(), color='green') #color: define  cor do gráfico.
    #key: obtém as chaves do dicionário. values: obtém os valores do dicionário.
    plt.title("IRA dos Alunos") 
    plt.xlabel("Alunos") #rótulo do eixo X.
    plt.ylabel("IRA") #rótulo do eixo Y.
    plt.show() #exibe o gráfico.

#função que exibe o menu e permite ao usuário escolher uma opção.
def menu():
    while True:
        print("""
          
Bem Vindo ao Mgre (Mostra Gráfica de Dados Escolares)
          
Estamos na fase inicial, porém já temos alguns dados
escolares da Instituição em que cituamos. Aproveite as
opções disponivéis abaixo e quem sabe nos deixe uma avaliação :)
              
Matérias que temos dados:
              
- matemática
- português
- ciências
- história
- geografia
                          
""")
        print("Escolha uma opção:")
        print("1. Ver média das matérias")
        print("2. Ver IRA dos alunos")
        print("3. Ver notas dos alunos em uma matéria específica")
        print("0. Sair")
       
        escolha = input("Digite o número da opção desejada: ")
       
        if escolha == "1":
            imprimir_media_materias()
        elif escolha == "2":
            imprimir_ira()
        elif escolha == "3":
            materia = input("Digite o nome da matéria: ")
            imprimir_notas_materia(materia)
        elif escolha == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

#chamadas automáticas das funções:
print("Executando funções automaticamente...\n")

#executa automaticamente as funções para imprimir as médias das matérias e o IRA dos alunos.
imprimir_media_materias()
imprimir_ira()

#em seguida, chama o menu interativo para permitir que o usuário interaja com o programa.
menu()
