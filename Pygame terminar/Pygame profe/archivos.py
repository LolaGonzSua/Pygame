import csv
import json
import os 
from preguntas import *
from datetime import datetime

# Leer las preguntas desde el archivo CSV y devolverlas como una lista de diccionarios
def leer_preguntas_csv(nombre_archivo: str) -> list:
    lista_preguntas = []
    if os.path.exists("preguntas.csv"):
        with open("preguntas.csv", mode="r") as archivo:  
            archivo.readline()  # Leer la cabecera (no se usa)
            for linea in archivo:
                linea = linea.strip()  # Eliminar saltos de línea y espacios innecesarios
                lista_valores = linea.split(",")  # Separar por coma
                # Crear el diccionario directamente con los valores de la línea
                pregunta = {
                    "pregunta": lista_valores[0],
                    "respuesta_1": lista_valores[1],
                    "respuesta_2": lista_valores[2],
                    "respuesta_3": lista_valores[3],
                    "respuesta_4": lista_valores[4],
                    "respuesta_correcta": int(lista_valores[5])
                }
                lista_preguntas.append(pregunta)  # Agregar el diccionario a la lista
        return lista_preguntas
    else:
        return []  # Si el archivo no existe, retornar una lista vacía

def guardar_preguntas_csv(nombre_archivo: str, lista_preguntas: list) -> bool:
    if not lista_preguntas:
        return False
    
    # Abrir el archivo en modo escritura
    with open("preguntas.csv", "w", newline="") as archivo:
        # Escribir la cabecera manualmente
        archivo.write("pregunta,respuesta_1,respuesta_2,respuesta_3,respuesta_4,respuesta_correcta\n")
        
        # Escribir los datos de las preguntas
        for pregunta in lista_preguntas:
            # Crear la línea de texto para cada pregunta, separada por comas
            linea = f"{pregunta['pregunta']},{pregunta['respuesta_1']},{pregunta['respuesta_2']},{pregunta['respuesta_3']},{pregunta['respuesta_4']},{pregunta['respuesta_correcta']}\n"
            archivo.write(linea)
    
    return True


def guardar_datos_jugador_json(nombre_archivo: str, nombre: str, puntaje: int):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r") as archivo_json:
            lista_jugadores = json.load(archivo_json)
    else:
        lista_jugadores = []

    fecha_actual = datetime.now().strftime("%d/%m/%Y")

    nuevo_jugador = {   #registro jugador
        "nombre": nombre,
        "puntaje": puntaje,
        "fecha": fecha_actual
    }

    lista_jugadores.append(nuevo_jugador)

    with open(nombre_archivo, "w") as archivo_json:
        json.dump(lista_jugadores, archivo_json, indent=4, ensure_ascii=False)

    print(f"Datos guardados: {nombre} con {puntaje} puntos.")

def cargar_datos_jugadores_json(nombre_archivo: str) -> list:
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r") as archivo_json:
            lista_jugadores = json.load(archivo_json)
        return lista_jugadores
    else:
        return [] 