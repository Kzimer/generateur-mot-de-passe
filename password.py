#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
from random import randrange

parser = argparse.ArgumentParser()
parser.add_argument("-M", help="avec des lettres majuscules",
                    action="store_true")
parser.add_argument("-m", help="avec des lettres minuscules",
                    action="store_true")
parser.add_argument("-c", help="avec des chiffres",
                    action="store_true")
parser.add_argument("-s", help="avec des caractères spéciaux accessibles",
                    action="store_true")
parser.add_argument("-a", help="autoriser les caractères similaires 0 O I 1 l",
                    action="store_true")
parser.add_argument("-i", help="autoriser les caractères spéciaux difficiles d'accès # @ [ \ ] ^ ` { | } ~",
                    action="store_true")

parser.add_argument("-l", type=int, default=8,
                    help="longueur du mot de passe, de 4 à 64, par défaut 8")
parser.add_argument("-n", type=int, default=5,
                    help="nombre de mots de passe à générer, par défaut 5")

args = parser.parse_args()

minuscules = 'abcdefghijkmnopqrstuvwxyz'

majuscules = 'ABCDEFGHJKLMNPQRSTUVWXYZ'

symbolesAccessibles = '''!"$%&'()*+,-./:;<=>?'''
symbolesDifficiles = '#@[\]^`{|}~'

chiffres = '23456789'

if not (args.M | args.m | args.c | args.s):
    args.M = True
    args.m = True
    args.c = True
    args.s = True

if not (3 < args.l < 65):
    args.l = 8

if (args.n < 1):
    args.n = 5

caracteres = ''

if args.m:
    caracteres += minuscules

if args.M:
    caracteres += majuscules

if args.c:
    caracteres += chiffres

if args.s:
    caracteres += symbolesAccessibles
    if args.i:
        caracteres += symbolesDifficiles

if args.a:
    if args.M & args.m & args.c: 
        caracteres += "0OI1l"
    elif args.M & args.c:
        caracteres += "0OI1"
    elif args.m & args.c:
        caracteres += "1l"
    elif args.M & args.m:
        caracteres += "Il"

for i in xrange(args.n):
    print ''.join([caracteres[randrange(len(caracteres))] for j in xrange(args.l)])
