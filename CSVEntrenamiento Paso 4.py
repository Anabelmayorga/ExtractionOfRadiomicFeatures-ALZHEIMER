# Código modificado y extendido del código original máquinas de Vector Soporte (SVM) con Python por Joaquín Amat Rodrigo, disponible con licencia CC BY-NC-SA 4.0 en https://www.cienciadedatos.net/documentos/py24-svm-python.html

# Tratamiento de datos
import pandas as pd
import numpy as np
from tqdm import tqdm
from itertools import combinations
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, GridSearchCV
import warnings
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score


warnings.filterwarnings('ignore')

# Cargar datos
datos = pd.read_excel(r"C:\oasis_cs_freesurfer\dataset_total_406.xlsx")

# Diagnóstico binario
datos['diagnostico_bin'] = datos['diagnostico'].apply(lambda x: 1 if str(x) == '1' else 0)

# Obtener todas las columnas excepto 'paciente' y 'diagnostico'
columnas_validas = datos.columns.difference(['paciente', 'diagnostico','diagnostico_bin'])


# Generar todas las combinaciones posibles de pares de características
combinaciones_pares = list(combinations(columnas_validas, 2))

# Grid de hiperparámetros
param_grid = {
    'C': np.logspace(2, 6, 50
                     ),
}

# Lista para almacenar resultados
resultados_modelos = []
matrices_conf_para_plot = []

# Bucle sobre cada combinación de pares
for carac_x, carac_y in tqdm(combinaciones_pares, desc="Combinaciones de características"):
    try:
        # Selección de características
        X = datos[[carac_x, carac_y]].copy()
        y = datos['diagnostico_bin'].copy()

        # División en train y test
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, train_size=0.8, random_state=1234, shuffle=True
        )

        # Búsqueda por validación cruzada
        grid = GridSearchCV(
            estimator=SVC(kernel="rbf", gamma='scale', class_weight='balanced'),
            param_grid=param_grid,
            scoring='accuracy',
            n_jobs=-1,
            cv=8,
            verbose=0,
            return_train_score=True
        )

        # Ajustar el modelo
        grid.fit(X_train, y_train)

        # Predicción en test
        modelo = grid.best_estimator_
        predicciones = modelo.predict(X_test)
        accuracy = accuracy_score(
            y_true    = y_test,
            y_pred    = predicciones,
            normalize = True
           )
        recall = recall_score(y_test, predicciones, average=None)
        precision = precision_score(y_test, predicciones, average=None)
        f1 = f1_score(y_test, predicciones , average=None)
        matriz_conf = confusion_matrix(y_test, predicciones)
        matrices_conf_para_plot.append((carac_x, carac_y, matriz_conf))

        # Guardar resultados
        resultados_modelos.append({
            'Caracteristica_1': carac_x,
            'Caracteristica_2': carac_y,
            'Mejor_C': grid.best_params_['C'],
            'Accuracy_CV': grid.best_score_,
            'Accuracy_Test': accuracy,
            'Recall': recall,
            'Precision': precision,
            'F1_Score': f1
        })

    except Exception as e:
        print(f"Error con {carac_x} y {carac_y}: {e}")
        continue

# Convertir resultados a DataFrame
df_resultados = pd.DataFrame(resultados_modelos)

# Ordenar por mayor rendimiento en test
df_resultados.sort_values(by='Accuracy_Test', ascending=False, inplace=True)

# Guardar en Excel
df_resultados.to_excel("resultados_modelos_SVM.xlsx", index=False)

print(f"Análisis completado y resultados guardados en 'resultados_modelos_SVM.xlsx'")


import math

# Mostrar matrices de confusión en bloques de 20
matrices_por_pagina = 20
num_matrices = len(matrices_conf_para_plot)
num_paginas = math.ceil(num_matrices / matrices_por_pagina)

for pagina in range(num_paginas):
    inicio = pagina * matrices_por_pagina
    fin = min(inicio + matrices_por_pagina, num_matrices)
    subset = matrices_conf_para_plot[inicio:fin]

    cols = 4
    rows = (len(subset) + cols - 1) // cols

    fig, axes = plt.subplots(rows, cols, figsize=(cols*4, rows*4))
    axes = axes.flatten()

    for idx, (carac_x, carac_y, matriz) in enumerate(subset):
        ax = axes[idx]
        sns.heatmap(matriz, annot=True, fmt="d", cmap="Blues", cbar=False,
                    xticklabels=["Pred. 0", "Pred. 1"],
                    yticklabels=["Real 0", "Real 1"], ax=ax)
        ax.set_title(f"{carac_x} vs {carac_y}", fontsize=8)
        ax.set_xlabel("Predicción", fontsize=7)
        ax.set_ylabel("Real", fontsize=7)

    # Eliminar ejes vacíos
    for j in range(len(subset), len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.suptitle(f"Matrices de Confusión - Página {pagina+1}", fontsize=12)
    plt.subplots_adjust(top=0.93)
    plt.show()
