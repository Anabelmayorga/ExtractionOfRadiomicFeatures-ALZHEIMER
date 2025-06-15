from __future__ import print_function
import six
import os  # needed navigate the system to get the input data
import pandas as pd
import SimpleITK as sitk

import radiomics
from radiomics import featureextractor  # This module is used for interaction with pyradiomics

# Definir la ruta de los archivos .nii
image_path = r"C:\oasis_cs_freesurfer\ARCHIVOS NIFTI\0309\brain.finalsurfs.nii\brain.finalsurfs.nii"
mask_path = r"C:\oasis_cs_freesurfer\ARCHIVOS NIFTI\0309\aseg.nii\aseg.nii"

# Instanciar el extractor de características
paramPath = r"C:\Users\Internet\Desktop\PYTHON TFG\Params.yaml"
extractor = featureextractor.RadiomicsFeatureExtractor(paramPath)

print('Enabled features:\n\t', extractor.enabledFeatures)

try:
    result = extractor.execute(image_path, mask_path)
    df_results = pd.DataFrame([result])
    df_results.to_csv("resultados_características_53_0309.csv", index=False)
    print("Extracción completada")
except Exception as e:
    print("Error durante la extracción")
