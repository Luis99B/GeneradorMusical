# Luis Bodart    A01635000
# Generador Musical con cadenas de Markov

'''
https://github.com/Luis99B/GeneradorMusical
'''

import random as r
import winsound as sound
import numpy as np

'''
--- Octava ---
    - DO
    - DO SOSTENIDO (#) / RE BEMOL (♭)
    - RE
    - RE SOSTENIDO (#) / MI BEMOL (♭)
    - MI
    - FA
    - FA SOSTENIDO (#) / SOL BEMOL (♭)
    - SOL
    - SOL SOSTENIDO (#) / LA BEMOL (♭)
    - LA
    - LA SOSTENIDO (#) / SI BEMOL (♭)
    - SI
'''

# octava 3 (menor) - (frecuencia, nombre)
oct3 = [
    (130.8128, "DO"), (138.5913, "DO#/REb"),
    (146.8324, "RE"), (155.5635, "RE#/MIb"),
    (164.8138, "MI"),
    (174.6141, "FA"), (184.9972, "FA#/SOLb"),
    (195.9977, "SOL"), (207.6523, "SOL#/LAb"),
    (220.0000, "LA"), (233.0819, "LA#/SIb"),
    (246.9417, "SI")
]

# octava 4 (mayor) - (frecuencia, nombre)
oct4 = [
    (261.6256, "DO"), (277.1826, "DO#/REb"),
    (293.6648, "RE"), (311.1270, "RE#/MIb"),
    (329.6276, "MI"),
    (349.2282, "FA"), (369.9944, "FA#/SOLb"),
    (391.9954, "SOL"), (415.3047, "SOL#/LAb"),
    (440.0000, "LA"), (466.1638, "LA#/SIb"),
    (493.8833, "SI")
]

# nombre de los estados
estados = [
    "DO", "DO#/REb",
    "RE", "RE#/MIb",
    "MI",
    "FA", "FA#/SOLb",
    "SOL", "SOL#/LAb",
    "LA", "LA#/SIb",
    "SI"
]

# nombre de las transiciones
transiciones = [
    [
        "DO -> DO", "DO -> DO#/REb",
        "DO -> RE", "DO -> RE#/MIb",
        "DO -> MI",
        "DO -> FA", "DO -> FA#/SOLb",
        "DO -> SOL", "DO -> SOL#/LAb",
        "DO -> LA", "DO -> LA#/SIb",
        "DO -> SI"
    ],
    [
        "DO#/REb -> DO", "DO#/REb -> DO#/REb",
        "DO#/REb -> RE", "DO#/REb -> RE#/MIb",
        "DO#/REb -> MI",
        "DO#/REb -> FA", "DO#/REb -> FA#/SOLb",
        "DO#/REb -> SOL", "DO#/REb -> SOL#/LAb",
        "DO#/REb -> LA", "DO#/REb -> LA#/SIb",
        "DO#/REb -> SI"
    ],
    [
        "RE -> DO", "RE -> DO#/REb",
        "RE -> RE", "RE -> RE#/MIb",
        "RE -> MI",
        "RE -> FA", "RE -> FA#/SOLb",
        "RE -> SOL", "RE -> SOL#/LAb",
        "RE -> LA", "RE -> LA#/SIb",
        "RE -> SI"
    ],
    [
        "RE#/MIb -> DO", "RE#/MIb -> DO#/REb",
        "RE#/MIb -> RE", "RE#/MIb -> RE#/MIb",
        "RE#/MIb -> MI",
        "RE#/MIb -> FA", "RE#/MIb -> FA#/SOLb",
        "RE#/MIb -> SOL", "RE#/MIb -> SOL#/LAb",
        "RE#/MIb -> LA", "RE#/MIb -> LA#/SIb",
        "RE#/MIb -> SI"
    ],
    [
        "MI -> DO", "MI -> DO#/REb",
        "MI -> RE", "MI -> RE#/MIb",
        "MI -> MI",
        "MI -> FA", "MI -> FA#/SOLb",
        "MI -> SOL", "MI -> SOL#/LAb",
        "MI -> LA", "MI -> LA#/SIb",
        "MI -> SI"
    ],
    [
        "FA -> DO", "FA -> DO#/REb",
        "FA -> RE", "FA -> RE#/MIb",
        "FA -> MI",
        "FA -> FA", "FA -> FA#/SOLb",
        "FA -> SOL", "FA -> SOL#/LAb",
        "FA -> LA", "FA -> LA#/SIb",
        "FA -> SI"
    ],
    [
        "FA#/SOLb -> DO", "FA#/SOLb -> DO#/REb",
        "FA#/SOLb -> RE", "FA#/SOLb -> RE#/MIb",
        "FA#/SOLb -> MI",
        "FA#/SOLb -> FA", "FA#/SOLb -> FA#/SOLb",
        "FA#/SOLb -> SOL", "FA#/SOLb -> SOL#/LAb",
        "FA#/SOLb -> LA", "FA#/SOLb -> LA#/SIb",
        "FA#/SOLb -> SI"
    ],
    [
        "SOL -> DO", "SOL -> DO#/REb",
        "SOL -> RE", "SOL -> RE#/MIb",
        "SOL -> MI",
        "SOL -> FA", "SOL -> FA#/SOLb",
        "SOL -> SOL", "SOL -> SOL#/LAb",
        "SOL -> LA", "SOL -> LA#/SIb",
        "SOL -> SI"
    ],
    [
        "SOL#/LAb -> DO", "SOL#/LAb -> DO#/REb",
        "SOL#/LAb -> RE", "SOL#/LAb -> RE#/MIb",
        "SOL#/LAb -> MI",
        "SOL#/LAb -> FA", "SOL#/LAb -> FA#/SOLb",
        "SOL#/LAb -> SOL", "SOL#/LAb -> SOL#/LAb",
        "SOL#/LAb -> LA", "SOL#/LAb -> LA#/SIb",
        "SOL#/LAb -> SI"
    ],
    [
        "LA -> DO", "LA -> DO#/REb",
        "LA -> RE", "LA -> RE#/MIb",
        "LA -> MI",
        "LA -> FA", "LA -> FA#/SOLb",
        "LA -> SOL", "LA -> SOL#/LAb",
        "LA -> LA", "LA -> LA#/SIb",
        "LA -> SI"
    ],
    [
        "LA#/SIb -> DO", "LA#/SIb -> DO#/REb",
        "LA#/SIb -> RE", "LA#/SIb -> RE#/MIb",
        "LA#/SIb -> MI",
        "LA#/SIb -> FA", "LA#/SIb -> FA#/SOLb",
        "LA#/SIb -> SOL", "LA#/SIb -> SOL#/LAb",
        "LA#/SIb -> LA", "LA#/SIb -> LA#/SIb",
        "LA#/SIb -> SI"
    ],
    [
        "SI -> DO", "SI -> DO#/REb",
        "SI -> RE", "SI -> RE#/MIb",
        "SI -> MI",
        "SI -> FA", "SI -> FA#/SOLb",
        "SI -> SOL", "SI -> SOL#/LAb",
        "SI -> LA", "SI -> LA#/SIb",
        "SI -> SI"
    ]
]

# probabilidades de las transiciones
probabilidades = [
    [
        0.123, 0.151,
        0.170, 0.065,
        0.026,
        0.137, 0.053,
        0.145, 0.023,
        0.034, 0.047,
        0.026
    ],
    [
        0.084, 0.117,
        0.079, 0.172,
        0.134,
        0.009, 0.064,
        0.055, 0.043,
        0.046, 0.112,
        0.085
    ],
    [
        0.110, 0.008,
        0.102, 0.083,
        0.115,
        0.185, 0.000,
        0.076, 0.084,
        0.057, 0.032,
        0.148
    ],
    [
        0.012, 0.026,
        0.103, 0.175,
        0.160,
        0.046, 0.059,
        0.124, 0.138,
        0.060, 0.097,
        0.000
    ],
    [
        0.028, 0.152,
        0.009, 0.008,
        0.135,
        0.015, 0.000,
        0.203, 0.142,
        0.169, 0.103,
        0.036
    ],
    [
        0.000, 0.168,
        0.118, 0.123,
        0.074,
        0.000, 0.087,
        0.100, 0.103,
        0.097, 0.037,
        0.093
    ],
    [
        0.166, 0.111,
        0.035, 0.114,
        0.105,
        0.065, 0.001,
        0.010, 0.113,
        0.112, 0.106,
        0.062
    ],
    [
        0.000, 0.000,
        0.128, 0.139,
        0.103,
        0.128, 0.097,
        0.034, 0.098,
        0.237, 0.007,
        0.029
    ],
    [
        0.000, 0.052,
        0.130, 0.160,
        0.146,
        0.000, 0.000,
        0.101, 0.000,
        0.196, 0.072,
        0.143
    ],
    [
        0.141, 0.072,
        0.058, 0.016,
        0.054,
        0.110, 0.109,
        0.115, 0.000,
        0.115, 0.128,
        0.082
    ],
    [
        0.028, 0.058,
        0.102, 0.006,
        0.122,
        0.003, 0.165,
        0.081, 0.003,
        0.145, 0.136,
        0.151
    ],
    [
        0.178, 0.042,
        0.036, 0.059,
        0.000,
        0.146, 0.036,
        0.101, 0.138,
        0.164, 0.046,
        0.054
    ]
]

# generar probabilidades con una suma cercana a 1
def generarProbabilidades():
    probs = list()
    for i in range(12):
        n = 1
        while n > .185:
            n = round(r.random(), 3)
        probs.append(n)
    print(probs)
    print("suma %.3f" % sum(probs))

# validar que la suma de las probabilidades de cada transicion sea 1
def validarProbabilidades():
    for s in range(len(probabilidades)):
        prob = sum(probabilidades[s])
        if round(prob, 3) != 1:
            print("ERROR: La probabilidad total debe ser 1 en la transicion '%s ->'" % estados[s])
            print("Faltante %.3f" % round(1-prob, 3))
            exit(1)

# generar la cadena de notas para reproducir las notas usando cadenas de Markov
def generarNotas(n = 8):
    if n < 1:
        print("ERROR: El numero de notas debe ser mayor a 1")
        exit(2)
    notas = list()
    # generar primera nota
    i = r.randint(0, 11)
    notas.append(estados[i])
    # generar cadena usando la matriz a partir de la primera nota
    for c in range(1, n):
        trans = np.random.choice(transiciones[i], replace=True, p=probabilidades[i])
        notas.append(estados[i])
        #print("markov actual %s" % trans)
        i = transiciones[i].index(trans)
    return notas

# reproducir las notas generadas
def reproducirNotas(notas):
    print("Reproduciendo %d notas" % len(notas))
    # primera nota
    i = estados.index(notas[0])
    if round(r.random(), 1) < .5:
        print("3|%s" % estados[i], end="")
        sound.Beep(int(oct3[i][0]), 500)
    else:
        print("4|%s" % estados[i], end="")
        sound.Beep(int(oct4[i][0]), 500)
    # notas siguientes
    for n in range(1, len(notas)):
        i = estados.index(notas[n])
        if round(r.random(), 1) < .5:
            print(" -> 3|%s" % estados[i], end="")
            sound.Beep(int(oct3[i][0]), 500)
        else:
            print(" -> 4|%s" % estados[i], end="")
            sound.Beep(int(oct4[i][0]), 500)
    print()


# generarProbabilidades()
validarProbabilidades()
try:
    n = int(input("Numero de notas a reproducir: "))
except ValueError:
    notas = generarNotas()
else:
    notas = generarNotas(n)
reproducirNotas(notas)
