#!/usr/bin/python
# prueba_reconocimiento.py

import glob
from subprocess import call

# TODO: comparar con los nombres de archivo (levenshtein para los "-"?)
# TODO: escribir a JSON con -j
# TODO: script para instalar
if __name__ == '__main__':
    filenames = glob.glob('./imagenes-placas/*.jpg')
    for filename in filenames:
        print filename
        call(['alpr', '-d', filename])
        print '____________________________'
