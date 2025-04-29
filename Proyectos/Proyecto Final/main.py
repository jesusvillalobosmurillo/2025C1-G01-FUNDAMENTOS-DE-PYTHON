# Proyecto final curso de Introducción a la Programación en Python
# Universidad Castro Carazo
# Autor: Jesus Villalobos
# Fecha: 30-04-2025
# Descripción: Este script procesa un archivo Excel con datos de inscritos en un evento de ciclismo.

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del archivo Excel
archivo_excel = r'c:\Users\jesus\OneDrive\Documentos\GitHub\2025C1-G01-FUNDAMENTOS-DE-PYTHON\Proyectos\Proyecto Final\Inscritos.xlsx'
df = pd.read_excel(archivo_excel, sheet_name='Hoja 1')

df = df.drop(df.columns[11:], axis=1)


df.head ()  # Mostrar las primeras 10 filas del DataFrame

# #Crear columnas específicas con datos relevantes
nombre = df['nombre'] # Columna de nombres
tipo_bici = df['bici'] # Columna de tipo de bicicleta
talla_jersey = df['talla'] # Columna de talla de jersey
color_jersey = df['color']  # Columna de color de jersey
hombre = df['hombre']  # Columna de hombres
mujer = df['mujer'] # Columna de mujeres

#Conteo de colores de jersey
color_jersey = color_jersey.str.split().str[0].str.lower()  # Procesar para obtener colores únicos
colores = color_jersey.value_counts() # Contar colores

print(f"\nCantidad de camisas por colores:")
print(colores)

#Conteo de tipos de bicicleta
tipo_bici = tipo_bici.str.lower()  # Cambiar a minusculas 
bicicletas = tipo_bici.value_counts() # Contar tipos de bicicletas

print(f"\nCantidad de bicicletas por tipo:")
print(bicicletas)

#Conteo de tallas de jersey
talla_jersey = talla_jersey.str.lower()  # Cambiar a minusculas las tallas
tallas = talla_jersey.value_counts() # Contar tallas de jerseys

print(f"\nCantidad de camisas por talla:")
print(tallas)

#Cantidad de hombres y mujeres
hombres = hombre.value_counts()  # Contar hombres   
mujeres = mujer.value_counts()  # Contar mujeres
print(f"\nCantidad de hombres: {hombres}")
print(f"\nCantidad de mujeres: {mujeres}")

#Separar los datos por género
datos_hombres = df[df['hombre'] == 1]  # Filtrar datos de hombres
datos_mujeres = df[df['mujer'] == 2]  # Filtrar datos de mujeres
#Procesar las tallas de jersey para hombres y mujeres
tallas_hombres = datos_hombres.iloc[:, 9].str.lower().value_counts().sort_index()
tallas_mujeres = datos_mujeres.iloc[:, 9].str.lower().value_counts().sort_index()

#Procesar los colores de jersey para hombres y mujeres
colores_hombres = datos_hombres['color'].str.split().str[0].str.lower().value_counts().sort_index()
colores_mujeres = datos_mujeres['color'].str.split().str[0].str.lower().value_counts().sort_index()

#Mostrar los resultados
print(f"\nTallas de camisas por género:")
print(f"\nHombres:")
print(tallas_hombres)
print(f"\nMujeres:")
print(tallas_mujeres)

print(f"\nColores de camisas por género:")
print(f"\nHombres:")
print(colores_hombres)
print(f"\nMujeres:")
print(colores_mujeres)

#Se crea un DataFrame para combinar tallas y colores para hombres
tallas_colores_hombres = pd.DataFrame({
    'Tallas': datos_hombres['talla'].str.lower(),
    'Colores': datos_hombres['color'].str.split().str[0].str.lower()
})

#Se crea un DataFrame para combinar tallas y colores para mujeres
tallas_colores_mujeres = pd.DataFrame({
    'Tallas': datos_mujeres['talla'].str.lower(),
    'Colores': datos_mujeres['color'].str.split().str[0].str.lower()
})

#Mostrar los resultados combinados
print(f"\nHombres: Tallas y Colores")
print(tallas_colores_hombres.value_counts().sort_index())

print(f"\nMujeres: Tallas y Colores")
print(tallas_colores_mujeres.value_counts().sort_index())

#Graficar la cantidad de participantes
plt.figure(figsize=(8, 8))
plt.pie([hombres.sum(), mujeres.sum()], labels=['Hombres', 'Mujeres'], autopct='%1.1f%%', startangle=80, colors=plt.cm.tab20.colors[:2])
plt.title('Porcentajes de Participantes')
plt.axis('equal')  # Asegurar que el gráfico sea un círculo
plt.tight_layout()
plt.show()

#Graficar la cantidad de bicicletas por tipo
plt.figure(figsize=(8, 8))
plt.pie(bicicletas.values, labels=bicicletas.index, autopct='%1.1f%%', startangle=80, colors=plt.cm.Paired.colors)
plt.title('Bicicletas por Tipo')
plt.axis('equal')  # Asegurar que el gráfico sea un círculo
plt.tight_layout()
plt.show()

#Grafica de la cantidad de camisas por color
plt.figure(figsize=(8, 8)) 
plt.pie(colores.values, labels=colores.index, autopct='%1.1f%%', startangle=80, colors=plt.cm.tab20.colors)
plt.title('Colores de Camisas')
plt.axis('equal')  # Asegurar que el gráfico sea un círculo
plt.tight_layout()
plt.show()

# Grafica de tallas para mujeres
plt.figure(figsize=(8, 8))
plt.bar(tallas_mujeres.index, tallas_mujeres.values, color=plt.cm.tab20.colors[:len(tallas_mujeres)])   
plt.title('Tallas de Camisas para Mujeres')
plt.xlabel('Tallas')
plt.ylabel('Cantidad')
plt.tight_layout()
plt.show()

# Grafica de tallas para hombres
plt.figure(figsize=(8, 8))
plt.bar(tallas_hombres.index, tallas_hombres.values, color=plt.cm.tab20.colors[:len(tallas_hombres)])
plt.title('Tallas de Camisas para Hombres')
plt.xlabel('Tallas')
plt.ylabel('Cantidad')
plt.tight_layout()
plt.show()
#Fin del script