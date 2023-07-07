# Codigo python que agrega ; al final de cada linea de un archivo csv 
#(Necesario para ser ingresado en una DB)

def csv_valido(nombre_archivo):
    # Leer el contenido del archivo CSV
    with open(nombre_archivo, 'r') as archivo_csv:
        lineas = archivo_csv.readlines()
    
    # Abrir el archivo CSV en modo escritura
    with open(nombre_archivo, 'w') as archivo_csv:
        # Recorrer cada línea del archivo
        for i, linea in enumerate(lineas):
            # Eliminar espacios en blanco al final de la línea
            linea = linea.rstrip()
            
            # Agregar el carácter ";" al final de la línea, excepto en la última línea
            if i < len(lineas) - 1:
                linea += ";"
            
            # Escribir la línea modificada en el archivo
            archivo_csv.write(linea + '\n')


# Ejemplo de uso
#int_archivo = "FUNDADORES"  # Reemplaza "datos.csv" por el nombre de tu archivo CSV
int_archivo = input("Agregue el archivo csv que desea le agregar el ;(AL FINAL DE CADA LINEA)\n: ")

csv_valido(int_archivo+".csv")
print("El archivo modificado exitosamente fue: ",int_archivo)
