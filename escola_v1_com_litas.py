#!/usr/bin/env python3
""" Exibe relatorio de crianas por atividade

Imprimir a lista de criancas agrupadas por sala que frequenta cada uma 
das atividades.
"""

__version__ = "0.1.0"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Ingles", aula_ingles),
    ("Musica", aula_musica), 
    ("Danca", aula_danca),
]

# Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades:
    
    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)

    print(f"{nome_atividade} Sala1: ", atividade_sala1)
    print(f"{nome_atividade} Sala2: ", atividade_sala2)
    print()
