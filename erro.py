#!/usr/bin/env python3

import os
import sys

#EAFP - Easy to ask Forgiveness than permission (é mais facil pedir perdão do que permissão

try:
    names = open("name.txt").readlines()
except:
    print("[ERROR] FILE name.txt not found.")
    sys.exit(1)


try:
    print(names[1])
except:
    print("[ERROR] Missing name in the list")
    sys.exit(1)

# LBYL - LOOK BEFORE YOU LEAP
