import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def filter_data(df: pd.DataFrame, year: int = None) -> pd.DataFrame:
    """Filtra los datos por el año proporcionado."""
    if year:
        return df[df["Período"] == year]
    return df

def generate_graph(df: pd.DataFrame) -> str:
    # Establecer el ancho de las barras
    bar_width = 0.3
    bar_width2 = 0.3
    # Posiciones de las barras en el eje X para los dos conjuntos de datos
    index = np.arange(len(df))
    
    # Crear el gráfico de barras agrupadas
    plt.figure(figsize=(10, 6))
    plt.bar(index, df["Porcentaje población en edad de trabajar"], bar_width, label="Tasa de edad trabajar (%)", color='skyblue')
    plt.bar(index + bar_width2,df["Tasa general de participación"] , bar_width2, label="Tasa General de Participación (%) ", color='salmon')

    # Etiquetas y título
    plt.xlabel("Año")
    plt.ylabel("Porcentaje (%)")
    plt.title("Comparación entre Tasa General de Participación y Tasa de edad para trabajar")
    plt.xticks(index + bar_width / 2, df["Período"])  # Posición de los valores del eje X (Años)
    plt.legend()
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)

    # Guardar gráfico
    graph_path = "static/graph.png"
    plt.savefig(graph_path)
    plt.close()
    return "/" + graph_path

def generate_summary_graph(df: pd.DataFrame) -> str:
    plt.figure(figsize=(10, 6))
    plt.plot(df["Período"], df["Tasa de desempleo"], marker="o", color="blue")
    
    plt.xlabel("Año")
    plt.ylabel("Tasa de Desempleo (%)")
    plt.title("Tasa de Desempleo Colombia (2019-2023)")
    plt.legend()
    plt.grid(True)

    # Guardar gráfico
    graph_path = "static/summary_graph.png"
    plt.savefig(graph_path)
    plt.close()
    return "/" + graph_path

def generate_population_growth_graph(df: pd.DataFrame) -> str:
    plt.figure(figsize=(10, 6))
    
    # Graficar el crecimiento de la población
    plt.plot(df["Período"], df["Población Colombia"], marker="o", color="green")
    
    plt.xlabel("Año")
    plt.ylabel("Población")
    plt.title("Crecimiento de la Población en Colombia (2019-2023)")
    plt.legend()
    plt.grid(True)

    # Guardar gráfico
    population_graph = "static/population_growth_graph.png"
    plt.savefig(population_graph)
    plt.close()
    return "/" + population_graph

def generate_comparation__graph(df: pd.DataFrame) -> str:

    plt.figure(figsize=(10, 6))
    
    # Graficar el crecimiento de la población
    plt.plot(df["Período"], df["Población en edad de trabajar"], marker="o", color="red", label="poblacion edad trabajar")
    plt.plot(df["Período"], df["Población económicamente activa"], marker="o", color="purple" , label="poblacion economicamente activa")
    
    plt.xlabel("Año")
    plt.ylabel("Población")
    plt.title("comparacion poblacion economicamente activa y en edad para trabajar Colombia (2019-2023)")
    plt.legend()
    plt.grid(True)

    # Guardar gráfico
    comparation_graph = "static/comparation_graph.png"
    plt.savefig(comparation_graph)
    plt.close()
    return "/" + comparation_graph



