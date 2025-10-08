"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd
import os

def pregunta_13():
    base_path = os.path.dirname(os.path.dirname(__file__))
    
    # Cargar archivos
    tbl0 = pd.read_csv(os.path.join(base_path, "files", "input", "tbl0.tsv"), sep="\t")
    tbl2 = pd.read_csv(os.path.join(base_path, "files", "input", "tbl2.tsv"), sep="\t")

    # Hacer merge usando c0 como clave
    merged = pd.merge(tbl0, tbl2, on="c0")

    # Agrupar por c1 y sumar c5b
    resultado = merged.groupby("c1")["c5b"].sum()

    return resultado

    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """