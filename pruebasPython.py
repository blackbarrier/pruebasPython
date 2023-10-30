
# open devuelve un objeto archivo 
archivo= open("texto.txt", encoding="utf-8")

lineas=archivo.readlines()
print(lineas)