- Este repositorio contiene el código y los datos empleados en el Trabajo de Fin de Grado (TFG) titulado:
“Extracción y clasificación de imágenes biomédicas cerebrales para la identificación de anomalías"

- Descripción del proyecto
El objetivo de este proyecto es desarrollar un sistema de ayuda al diagnóstico asistido por computadora (CAD) para la detección de la Enfermedad de Alzheimer, mediante el análisis de imágenes de resonancia magnética (MRI) cerebrales, utilizando técnicas de radiómica para la extracción de características morfológicas y de textura, centradas en el hipocampo como región de interés (ROI).

Posteriormente, estas características son clasificadas mediante algoritmos de aprendizaje automático, concretamente máquinas de soporte vectorial (SVM), con el fin de identificar de forma temprana a los pacientes con EA.

Se ha utilizado la base de datos pública OASIS-1 (Open Access Series of Imaging Studies), la cual proporciona imágenes de resonancia magnética cerebral de pacientes sanos y con diagnóstico de Alzheimer.

- Metodología
Preprocesamiento y segmentación: Las imágenes han sido preprocesadas y segmentadas mediante herramientas como FreeSurfer, por OASIS-1, seleccionando el hipocampo como ROI.

Extracción de características: Se han calculado características radiómicas siguiendo el estándar IBSI (Zwanenburg et al., 2020), incluyendo variables de forma, intensidad y textura (GLCM, GLSZM, etc.).

Clasificación: Se han entrenado modelos de SVM utilizando combinaciones de pares de características radiómicas para evaluar su rendimiento diagnóstico.

Evaluación: Las métricas de rendimiento incluyen accuracy, precision, recall y F1-Score, obteniendo resultados prometedores tanto en el hipocampo derecho como izquierdo.


- Este proyecto ha sido desarrollado en Python 3.8.

- Licencia
Este proyecto está publicado bajo licencia MIT. Puedes consultarla en el archivo LICENSE.

- Autor
Trabajo de Fin de Grado (TFG) realizado por Anabel Mayorga Ruiz
Facultad de Ciencias — Universidad de Córdoba
Año académico: 2025
