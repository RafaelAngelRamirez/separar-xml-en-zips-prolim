from ast import While

from os import listdir, path, makedirs
from os.path import isfile, join
import subprocess


import math

mypath = 'xml'
carpeta_comprimidos = 'ficheros_comprimidos'
exist = path.exists(carpeta_comprimidos)
if not exist:
    makedirs(carpeta_comprimidos)

onlyfiles = [f'{mypath}/{f}' for f in listdir(mypath) if isfile(join(mypath, f))]

contador = 0
limite = 500

total_de_ficheros = len(onlyfiles)
total_de_zips = math.ceil(total_de_ficheros/limite)


for vuelta in range(1, total_de_zips+1):
    print(f'[ INFO ] Procesando vuelta {vuelta} - contador {contador}')
    ficheros_a_comprimir = onlyfiles[contador:limite+contador]
    comando_zip = f'zip {carpeta_comprimidos}/xml{vuelta}.zip  {" ".join(ficheros_a_comprimir)} '
    subprocess.call(comando_zip, shell=True)
    contador += limite

print('[!] Termino')

