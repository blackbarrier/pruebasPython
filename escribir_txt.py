
#En este caso vamos a realizar la escitura. Donde debemos
#incorporar el parametro "w" (write), para permitir la
#escritura. Esto se llama modo. Para leer se utiliza "r"
#pero como es el modo por defecto a veces no se escribe.

# with open("texto_creado.txt", "w", encoding="utf-8") as archivo:
#     archivo.write("LCDTM")


#WiteLines

with open("texto_creado.txt", "w", encoding="utf-8") as archivo:
    archivo.writelines(["Hola\n", "Estoy escribiendo"])
    print(archivo.read)