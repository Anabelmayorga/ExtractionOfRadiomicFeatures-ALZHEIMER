import os
import nibabel as nib
# Ruta de la carpeta de origen (donde están los archivos .mgz)
source_dir = r"C:\oasis_cs_freesurfer\disc1\OAS1_0368_MR2"

# Ruta de destino (donde se guardarán los archivos NIFTI convertidos)
destination_dir = r"C:\oasis_cs_freesurfer\ARCHIVOS NIFTI\0368"

# Función para convertir .mgz a .nii.gz
def convert_mgz_to_nifti(mgz_file, output_path):
    try:
        # Cargar el archivo MGZ con nibabel
        img = nib.load(mgz_file)
        
        # Guardar el archivo en formato NIFTI (.nii.gz)
        nib.save(img, output_path)
        print(f"Archivo convertido y guardado: {output_path}")
    except Exception as e:
        print(f"Error al convertir {mgz_file}: {e}")

# Crear el directorio de destino si no existe
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Recorrer todas las subcarpetas y archivos dentro de source_dir
for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file.lower().endswith(".mgz"):  # Verificar si el archivo tiene la extensión .mgz
            # Crear la ruta completa del archivo .mgz
            mgz_path = os.path.join(root, file)
            
            # Obtener la parte del nombre del archivo sin la extensión
            base_name = os.path.splitext(file)[0]
            
            # Crear la ruta de salida para el archivo convertido
            output_file_name = f"{base_name}.nii.gz"
            output_path = os.path.join(destination_dir, output_file_name)
            
            # Convertir el archivo .mgz a .nii.gz
            convert_mgz_to_nifti(mgz_path, output_path)