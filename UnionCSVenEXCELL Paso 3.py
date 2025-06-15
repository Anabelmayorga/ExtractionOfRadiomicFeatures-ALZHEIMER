import pandas as pd
import os

# Ruta de la carpeta donde están los CSVs
carpeta = r"C:\oasis_cs_freesurfer\ARCHIVOS CSV EXTRACCION\HIPOCAMPO IZQUIERDO"

# Lista de columnas que quieres conservar
columnas_deseadas = [
    'original_shape_MeshVolume',
    'original_shape_SurfaceArea',
    'original_firstorder_Energy',
    'original_firstorder_Entropy',
    'original_firstorder_Mean',
    'original_firstorder_Skewness',
    'original_firstorder_Kurtosis',
    'original_firstorder_Variance',
    'original_glcm_Autocorrelation',
    'original_glcm_ClusterShade',
    'original_glcm_ClusterProminence',
    'original_glcm_Correlation',
    'original_glcm_SumAverage',
    'original_glcm_SumEntropy',
    'original_glcm_SumSquares',
    'original_glcm_DifferenceVariance',
    'original_glcm_DifferenceEntropy',
    'original_glcm_Imc1',
    'original_glcm_Imc2',
    'original_glszm_SmallAreaLowGrayLevelEmphasis',
    'original_glszm_SmallAreaHighGrayLevelEmphasis',
    'original_glszm_LargeAreaLowGrayLevelEmphasis',
    'original_glszm_LargeAreaHighGrayLevelEmphasis',
    'original_glszm_SizeZoneNonUniformity',
    'original_glszm_GrayLevelNonUniformity'
]

# Crear lista para almacenar los DataFrames
dataframes = []

# Recorrer todos los archivos .csv en la carpeta
for archivo in os.listdir(carpeta):
    if archivo.endswith(".csv"):
        ruta_completa = os.path.join(carpeta, archivo)
        df = pd.read_csv(ruta_completa)

        # Seleccionar solo las columnas deseadas
        df_filtrado = df[columnas_deseadas].copy()

        # Añadir una columna con el nombre del archivo (ID del paciente)
        df_filtrado["paciente"] = os.path.splitext(archivo)[0]

        # Añadir al conjunto
        dataframes.append(df_filtrado)

# Unir todos los dataframes en uno solo
df_final = pd.concat(dataframes, ignore_index=True)

# Guardar a Excel
df_final.to_excel("dataset_total.xlsx", index=False, engine='openpyxl')

print("✅ Dataset combinado guardado como 'dataset_total.xlsx'")
