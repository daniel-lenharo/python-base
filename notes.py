#!/usr/bin/env python3

"""
Bloco de Notas

$notes.py new "Minha note"

tag: tech
text: blablablabla


"""

__version__ = "0.1.0"

from ast import arguments
from ntpath import join
import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    sys.exit(1)

cmds = ("read","")
if arguments[0] not in cmds:
    print(f"invalid command {arguments[0]}")

if arguments[0] == "read":
    # leitura das notas
    for line in open(filepath):
        titulo, tag, texto = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"titulo: {titulo}")
            print(f"text: {text}")
            print("-" * 30)
    pass

if arguments[0] == "new":
    titulo = arguments[1] 
    text = [
        f"{titulo}",
        input("tag:").strip(),
        input("text:\n").strip(),
        "\n"
    ]
    # \t - tsv
    with open(filepath, "a") as file_:
        file_.write("\t".join(text))
