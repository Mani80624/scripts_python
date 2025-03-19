import os

def listar_carpetas(directorio):
    try:
        carpetas = [nombre for nombre in os.listdir(directorio) if os.path.isdir(os.path.join(directorio, nombre))]
        return carpetas
    except Exception as e:
        print(f"Error al listar carpetas: {e}")
        return []