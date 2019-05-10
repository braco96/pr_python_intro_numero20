# -*- coding: utf-8 -*-
import re
def run(args):
    if not args:
        return "ayuda: use 'hola <nombre>'"
    if args[0]=="hola" and len(args)>1:
        return f"Hola, {args[1]}!"
    return "comando no reconocido"

