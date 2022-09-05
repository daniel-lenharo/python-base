#!/usr/bin/env python3
"""

"""
import logging
import sys

quartos = {}
try:
    for line in open("quarto.txt"):
        codigo, nome, preco = line.strip().split(",")
        quartos[codigo] = {
            "nome": nome,
            "preco": float(preco), #TODO: DECIMA
            "disponivel": True

        }
except FileNotFoundError:
    logging.error("Arquivo nao existe")
    sys.exit(1)

for codigo,dados in quartos.items():
    nome = dados["nome"]
    preco = dados["preco"]
    disponivel = "NOK" if not dados['disponivel'] else "OK"


    print(f"{codigo} - {nome} - R$ {preco:.2f} - {disponivel}")

print("-" * 40)

name = input("Nome do cliente:").strip()

try:
    num_quarto = int(input("Qual o quarto desejado?:").strip())
    if not quartos[num_quarto]["disponivel"]:
        printf(f"O quarto {num_quarto} está ocupado.")
        sys.exit(1)
except ValueError:
    logging.error("Numero invalido, digite apenas digitos.")
    sys.exit(1)

if num_quarto not in quartos:
    print("quarto escolhido inválido")

try:
    diarias = int(input("Qual a quantidade de diarias?:").strip())
except ValueError:
    logging.error("diarias invalidas, digite apenas digitos.")
    sys.exit(1)