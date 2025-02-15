import re

def limpiar_y_guardar(archivo_entrada, archivo_salida):
    patron = re.compile(r'[-–] ([^\(]+) \(([^)]+)\)$')
    
    with open(archivo_entrada, "r", encoding="utf-8") as entrada, open(archivo_salida, "w", encoding="utf-8") as salida:
        for linea in entrada:
            match = patron.search(linea)
            if match:
                traduccion = match.group(1).strip()  # Captura la traduccion
                romaji = match.group(2).strip()  # Captura el romaji
                salida.write(f"{romaji}, {traduccion}\n")


limpiar_y_guardar("palabras.txt", "palabras_traducidas.txt")