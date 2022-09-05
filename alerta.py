#!/usr/bin/env python3

'''
Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime
cada uma das palavras com suas vogais duplicadas.

Faça um script que pergunta ao usuário qual a temperatura atual e o indice de
umidade do ar sendo que caso será exibida uma mensagem de alerta dependendo
das condições:

temp maior 45: "ALERTA!!! 🥵 Perigo calor extremo"

temp maior que 30 e temp vezes 3 for maior ou igual a umidade:

"ALERTA!!! 🥵♒ Perigo de calor úmido"

temp entre 10 e 30: "😀 Normal"

temp entre 0 e 10: "🥶 Frio"

temp <0: "ALERTA!!! ⛄ Frio Extremo."

ex:

'''

import sys
import logging
from traceback import print_tb
log = logging.Logger("alerta")

info = {
    "temperatura": None,
    "umidade": None
}

for key in info.keys():
    try:
        info[key] = float(input(f"QUal a {key}?").strip())
    except ValueError:
        log.error(f"{key.capitalize()} inválida")
        sys.exit(1)

temp = info["temperatura"]
umidade = info["umidade"]

if temp > 45:
    print("ALERTA!! CALOR EXTREMO")
elif temp * 3 >= umidade:
    print("Alerta!! Perigo de Calor Umido")
elif temp >= 10 and temp <= 30:
    print("Normal")
elif temp >= 0 and temp <= 10:
    print("Frio")
elif temp <0:
    print("ALERTA! Frio extremo!")



print(info["temperatura"])
print(info["umidade"])