import pathlib
path = pathlib.Path('foobar.txt')
path.exists()

archi1=open("datos.txt","w")
# archi1 = open("E:\Data Science/datos.txt","w")
archi1.write("Primer línea.\n")
archi1.write("Segunda línea.\n")
archi1.write("Tercer línea.\n")
archi1.close()

archi1=open("datos.txt","r")
contenido=archi1.read()
print(contenido)
archi1.close()

archi1 = open('temp.txt')
print( archi1.readline() )
print( archi1.readline() )
print( archi1.readlines() )
archi1.close()

archi1=open("datos.txt","r")
linea=archi1.readline()
while linea!='':
    print(linea, end='')
    linea=archi1.readline()
archi1.close()

archi1=open("datos.txt","r")
for linea in archi1:
    print(linea, end='')
archi1.close()

archi1=open("datos.txt","r")
lineas=archi1.readlines()
print('El archivo tiene', len(lineas), 'líneas')
print('El contenido del archivo')
for linea in lineas:
    print(linea, end='')
archi1.close()

archi1=open("datos.txt","a")
archi1.write("nueva línea 1\n")
archi1.write("nueva línea 2\n")
archi1.close()
archi1=open("datos.txt","r")
contenido=archi1.read()
print(contenido)
archi1.close()

archi1=open("datos.txt","r+")
contenido=archi1.read()
print(contenido)
archi1.write("Otra línea 1\n")
archi1.write("Otra línea 2\n")
archi1.close()

archi1=open("datos.txt","w", encoding="utf-8")
archi1.write("Primer línea.\n")
archi1.write("Segunda línea.\n")
archi1.write("Tercer línea.\n")
archi1.close()

# open a file for reading
states = open('state_data.txt')
# open a new file for writing
capitals = open('capitals.txt', 'w')
# store the result of readlines() in a variable
states_list = states.readlines()
# loop over the list that resulted from readlines()
for state in states_list:
    foo = state.split('\t')               # split the line at the tabs
    text = foo[1] + ", " + foo[0] + '\n'  # create text: capital, state
    capitals.write(text)                  # write text into the new file
# close both files
capitals.close()
states.close()

with open('temp.txt', 'a') as f:
    words = "I would not like to eat any spam."
    f.write(words)

from urllib.request import urlopen
from bs4 import BeautifulSoup
page = urlopen("https://weimergeeks.com/examples/scraping/example1.html")
soup = BeautifulSoup(page, "html.parser")
print(soup.h1)








