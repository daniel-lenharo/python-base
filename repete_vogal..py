#!/usr/bin/env python3

'''
Faça um programa que pede ao usuário que digite uma ou mais palavras e
imprime cada uma das palavras com suas vogais duplicadas.

python repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Bruno
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Bruunoo

'''
words = []
while True:
    word = input("Digita uma palavra (ou enter para sair):").strip()
    if not word:
        break


    final_world = ""
    for letter in word:
        if letter.lower() in "aeiou":
            final_world += letter * 2
        else:
            final_world += letter
    words.append(final_world)


print(*words, sep="\n")

for word in words:
    print(word)