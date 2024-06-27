import matplotlib.pyplot as plt
def plot_barras(datos):
    frecuencias = {}
    for elemento in datos:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1
    
    frecuencias_ordenadas = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)
    
    labels = [x[0] for x in frecuencias_ordenadas]
    sizes = [x[1] for x in frecuencias_ordenadas]
    
    plt.figure(figsize=(12, 8))
    plt.barh(labels, sizes)
    plt.yticks(rotation=0)
    plt.title('Frecuencia de Elementos')
    plt.xlabel('Frecuencia')
    plt.ylabel('Elemento')
    plt.grid()
    plt.show()
    

def plot_pie(datos):
    frecuencias = {}
    for apellido in datos:
        if apellido in frecuencias:
            frecuencias[apellido] += 1
        else:
            frecuencias[apellido] = 1
    
    frecuencias_ordenadas = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)
    
    labels = [x[0] for x in frecuencias_ordenadas]
    sizes = [x[1] for x in frecuencias_ordenadas]
    
    plt.figure(figsize=(12, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')
    plt.title('Frecuencia de Apellidos')
    plt.show()