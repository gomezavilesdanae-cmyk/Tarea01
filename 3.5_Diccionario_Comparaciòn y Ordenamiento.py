import random
import string
import time


# --- 1. Implementación de Merge Sort (O(n log n)) ---
def merge_sort(arr):
  if len(arr) <= 1:
    return arr

  medio = len(arr) // 2
  izquierda = merge_sort(arr[:medio])
  derecha = merge_sort(arr[medio:])

  return _mezclar(izquierda, derecha)


def _mezclar(izquierda, derecha):
  resultado = []
  i = j = 0

  while i < len(izquierda) and j < len(derecha):
    if izquierda[i] <= derecha[j]:
      resultado.append(izquierda[i])
      i += 1
    else:
      resultado.append(derecha[j])
      j += 1

  resultado.extend(izquierda[i:])
  resultado.extend(derecha[j:])
  return resultado


# --- 2. Implementación de Quick Sort (O(n log n) promedio) ---
def quick_sort(arr):
  if len(arr) <= 1:
    return arr

  pivote = arr[len(arr) // 2]
  menores = [x for x in arr if x < pivote]
  iguales = [x for x in arr if x == pivote]
  mayores = [x for x in arr if x > pivote]

  return quick_sort(menores) + iguales + quick_sort(mayores)


# --- 3. Generador de datos de prueba ---
def generar_lista_palabras(n):
  palabras = []
  for _ in range(n):
    longitud = random.randint(3, 8)
    palabra = ''.join(
        random.choices(string.ascii_lowercase, k=longitud)
    )
    palabras.append(palabra)
  return palabras


# --- 4. Ejecución del experimento empírico ---
def realizar_comparacion():
  tamanos = [100, 1000, 10000]
  resultados = []

  for tamano in tamanos:
    # Generar palabras aleatorias del tamaño objetivo
    datos_base = generar_lista_palabras(tamano)

    # Copias independientes para garantizar igualdad en las pruebas
    datos_merge = list(datos_base)
    datos_quick = list(datos_base)

    # Medición de tiempo para Merge Sort
    inicio = time.perf_counter()
    _ = merge_sort(datos_merge)
    fin = time.perf_counter()
    tiempo_merge = fin - inicio

    # Medición de tiempo para Quick Sort
    inicio = time.perf_counter()
    _ = quick_sort(datos_quick)
    fin = time.perf_counter()
    tiempo_quick = fin - inicio

    resultados.append({
        'tamano': tamano,
        'merge_sort_s': tiempo_merge,
        'quick_sort_s': tiempo_quick,
    })

  return resultados


if __name__ == '__main__':
  datos_experimento = realizar_comparacion()

  print(f"{'Tamaño (N)':<15}{'Merge Sort (seg)':<20}{'Quick Sort (seg)':<20}")
  print('-' * 55)
  for r in datos_experimento:
    print(
        f"{r['tamano']:<15}{r['merge_sort_s']:<20.6f}{r['quick_sort_s']:<20.6f}"
    )
