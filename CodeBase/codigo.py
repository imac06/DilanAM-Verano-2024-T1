import matplotlib.pyplot as plt
import numpy as np

def ordenar_asc(datos):
    arr_len = len(datos)
    for i in range(arr_len):
        min_idx = i
        for j in range(i+1, arr_len):
            if datos[j] < datos[min_idx]:
                min_idx = j
        datos[i], datos[min_idx] = datos[min_idx], datos[i]
    return datos

def frec_abs(datos):
    clases, fa_absoluta = [], []
    for elemento in datos:
        if elemento not in clases:
            clases.append(elemento)
            fa_absoluta.append(1)
        else:
            idx = clases.index(elemento)
            fa_absoluta[idx] += 1
    return clases, fa_absoluta  

def format_str(datos):
    d_formated = []
    for dato in datos:
        if isinstance(dato, str):
            dato_formateado = dato.upper().replace(" ", "")
            d_formated.append(dato_formateado)
        else:
            d_formated.append(dato)
    return d_formated

def calcular_limites(datos):
    frecuencias = frec_abs(datos)[1]
    limite_inferior = min(frecuencias)
    limite_superior = max(frecuencias)
    return limite_inferior, limite_superior

def calcular_frecuencia_relativa(datos):
    frecuencias_absolutas = frec_abs(datos)[1]
    total_elementos = len(datos)
    frecuencias_relativas = [f / total_elementos for f in frecuencias_absolutas]
    return frecuencias_relativas

def calcular_frecuencias_acumuladas(datos):
    frecuencias_absolutas = frec_abs(datos)[1]
    frecuencias_acumuladas = []
    acumulado = 0
    for frec in frecuencias_absolutas:
        acumulado += frec
        frecuencias_acumuladas.append(acumulado)
    return frecuencias_acumuladas

def plot_histograma(datos):
    datos_ordenados = ordenar_asc(datos[:])
    limite_inferior, limite_superior = calcular_limites(datos_ordenados)
    clases, fa_absoluta = frec_abs(datos_ordenados)
    frec_relativa = calcular_frecuencia_relativa(datos_ordenados)

    plt.figure(figsize=(8, 6))
    plt.bar(clases, frec_relativa, width=0.5, edgecolor='black')
    plt.xlabel('Marca de clase')
    plt.ylabel('Frecuencia relativa')
    plt.title('Histograma')
    plt.grid()
    plt.show()
    
def plot_ojiva(datos):
    datos_ordenados = ordenar_asc(datos[:])
    frec_acumulada = calcular_frecuencias_acumuladas(datos_ordenados)

    plt.figure(figsize=(8, 6))
    plt.plot([0] + frec_acumulada, range(0, len(frec_acumulada) + 1), marker='o')
    plt.xlabel('Frecuencia acumulada')
    plt.ylabel('Número de valores')
    plt.title('Gráfico de Ojiva')
    plt.grid()
    plt.show()

def plot_histogram2(datos, num_clases):
    plt.hist(datos, bins=num_clases, edgecolor='black')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.title('Histograma')
    plt.show()

def plot_ojiva2(datos, num_clases):
    frecuencias, bordes = np.histogram(datos, bins=num_clases)
    frecuencias_acumuladas = np.cumsum(frecuencias)
    ojiva = np.insert(frecuencias_acumuladas, 0, 0)
    plt.plot(bordes, ojiva, marker='o', linestyle='-')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia acumulada')
    plt.title('Ojiva')
    plt.grid()
    plt.show()

