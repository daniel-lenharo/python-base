#!/usr/bin/env python3

import os
import sys

if os.path.exists("name.txt"):
    names = open("name.txt").readlines()
else:
    print("[ERROR] FILE name.txt not found.")
    sys.exit(1)


if len(names) >=3:
    print(names[1])
else:
    print("[ERROR] Missing name in the list")
    sys.exit(1)

# LBYL - LOOK BEFORE YOU LEAP
