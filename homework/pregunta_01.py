"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    with open("files/input/clusters_report.txt", "r") as f:
        lines = f.readlines()

    data = lines[4:]

    texto = ""
    for line in data:
        line = line.strip()
        line = line.replace("\t", " ")

        while "  " in line:
            line = line.replace("  ", " ")

        if line:
            if line[0].isdigit():
                texto += "\n" + line
            else:
                texto += " " + line

    texto = texto.split("\n")
    datos = []

    for elem in texto[1:]:
        partes = elem.split(" ")

        cluster = int(partes[0])
        cantidad = int(partes[1])

        porcentaje = float(
            (partes[2] + ("" if "%" in partes[2] else partes[3]))
            .replace(",", ".")
            .replace("%", "")
        )

        palabras = " ".join(partes[4:] if "%" not in partes[2] else partes[3:])
        palabras = palabras.replace(".", "")

        datos.append([cluster, cantidad, porcentaje, palabras])

    df = pd.DataFrame(datos, columns=[
        "cluster",
        "cantidad_de_palabras_clave",
        "porcentaje_de_palabras_clave",
        "principales_palabras_clave"
    ])

    return df
  