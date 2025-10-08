"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import os
import pandas as pd


def pregunta_11():
    base_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_path, "files", "input", "tbl1.tsv")

    df = pd.read_csv(file_path, sep="\t")

    # Paso 1: Expandir c4 en filas separadas por c0
    df["c4"] = df["c4"].str.split(",")

    # Paso 2: Expandir cada valor de c4 en una fila (explode)
    df = df.explode("c4")

    # Paso 3: Agrupar por c0 y unir los valores de c4 ordenados
    resultado = (
        df.groupby("c0")["c4"]
        .apply(lambda x: ",".join(sorted(x)))
        .reset_index()
    )

    return resultado


    """
    Construya una tabla que contenga `c0` y una lista separada por ',' de
    los valores de la columna `c4` del archivo `tbl1.tsv`.

    Rta/
         c0       c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """