import os
import zipfile

def zip_directory(root_dir, source_dir, zipf):
    for root, _, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, root_dir)
            zipf.write(file_path, arcname=relative_path)

if __name__ == "__main__":
    source_directory = input("Ingresa la ruta del directorio fuente: ")
    output_filename = input("Ingresa el nombre del archivo ZIP de salida: ")

    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zip_directory(source_directory, source_directory, zipf)

    print("Archivo ZIP creado exitosamente.")