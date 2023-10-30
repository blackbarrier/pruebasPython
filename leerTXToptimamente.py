with open("texto_creado.txt", encoding="utf-8") as archivo:
    print(archivo.read())

# No es necesario cerrarlo. Con with cuando termina la
# instuccion lo cierra automaticamente   