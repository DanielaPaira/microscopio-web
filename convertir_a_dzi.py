import pyvips

# Nombre del archivo TIFF original
input_path = "Prueba1.tif"

# Nombre del resultado (.dzi y carpeta de tiles)
output_prefix = "Prueba1_dzi"

print("🔍 Cargando imagen...")
image = pyvips.Image.new_from_file(input_path, access="sequential")

print("🧩 Generando imagen Deep Zoom (.dzi)...")
image.dzsave(output_prefix)

print("✅ ¡Conversión completada!")

