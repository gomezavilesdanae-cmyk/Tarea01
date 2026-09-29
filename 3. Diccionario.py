# 3. Diccionario


# 1. Normalización de texto: Limpiar el texto de entrada.
# Creamos la clase excepción por si ingresan un texto vacío
class TextoVacioError(Exception):
    def __init__(self, mensaje="El texto está vacío."):
        self.mensaje = mensaje
        # Usamos super() para pasar el mensaje a la clase padre Exception
        super().__init__(self.mensaje)

# Creamos la clase NormalizadorTexto para convertir el texto a minúsculas, quitar acentos, etc.
class NormalizadorTexto:
    def normalizar(self, texto):
        # Por si el texto está vacío o son solo espacios, lanzamos el error
        if not texto.strip():
            raise TextoVacioError("El texto no puede estar vacío")

        # Pasar el texto a minúsculas
        texto_minusculas = texto.lower()

        # Creamos un diccionario para modificar las vocales con acento
        acentos_limpio = {'á': 'a', 'à': 'a',
                      'é': 'e', 'è': 'e',
                      'í': 'i', 'ì': 'i',
                      'ó': 'o', 'ò': 'o',
                      'ú': 'u', 'ù': 'u',
                      'ü': 'u',
                      }

        # Agregamos el abecedario permitido para poder quitar puntuación, símbolos, números, etc.
        abecedario = "abcdefghijklmnñopqrstuvwxyz"
        # Se comienza a armar la cadena limpia
        texto_limpio = ""

        # Recorremos caracter por caracter
        for letra in texto_minusculas:
            # Si la letra tiene acento, la cambiamos usando el diccionario
            if letra in acentos_limpio:
                letra = acentos_limpio[letra]

            # Si es una letra normal o un espacio, la guardamos como está
            if letra in abecedario or letra == " ":
                texto_limpio += letra
            # Si es puntuación, número, etc. ponemos un espacio para que no se peguen las palabras
            else:
                texto_limpio += " "

        # Regresamos el texto quitando los espacios sobrantes
        return texto_limpio.strip()


# 2 y 4. Hash y Frecuencias
        tabla = TablaFrecuencias() # Usamos la clase hija que incluye ambas funciones
        for palabra in texto_limpio.split():
            tabla.insertar(palabra)
            
        palabras_extraidas = tabla.obtener_solo_palabras()
# 2. Eliminación de repetidos con tabla hash propia y 4. Conteo de frecuencia
class TablaHashBase:
    def _init_(self, tamano=100):
        self.tamano = tamano
        # Buckets (listas) para manejar colisiones por encadenamiento
        self.buckets = [[] for _ in range(self.tamano)]

    def _hash(self, palabra):
        # Función hash simple: suma de valores ASCII módulo el tamaño
        suma = sum(ord(c) for c in palabra)
        return suma % self.tamano

    def insertar(self, palabra):
        indice = self._hash(palabra)
        bucket = self.buckets[indice]

        # Resolver colisiones iterando en el bucket para detectar repetidos
        for p in bucket:
            if p == palabra:
                # Si la palabra ya existe, detenemos la inserción (elimina repetidos)
                return 
        
        # Si no existe en el bucket, la agregamos
        bucket.append(palabra)

    def obtener_solo_palabras(self):
        resultado = []
        for bucket in self.buckets:
            for p in bucket:
                resultado.append(p)
        return resultado


# 3. Algoritmos de Ordenamiento (Merge Sort y Quick Sort) 
def merge_sort(lista):
    if len(lista)<=1:
        return lista
    mitad=len(lista)//2}
    izquierda=merge_sort(lista[:mitad])
    derecha=merge_sort(lista[mitad:])
    return mezclar(izquierda, derecha)

def mezclar(izquierda, derecha):
    resultado=[]
    i=0
    j=0
    while i<len(izquierda) and j<len(derecha):
        if izquierda[i]<=.append(izquierda[i])
            resultado.append(izquierda[i])
            i+=1
        else:
            resultado.append(derecha[j])
            j+=1
    while i<len(izquierda):
        resultado.append(izquierda[i])
        i+=1

    while j<len(derecha):
        resultado.append(derecha[j])
        j+=1
    return resultado
def quick_sort(lista):
    if len(lista)<=1:
        return lista

    pivote=lista[len(lista)//2]

    menor=[]
    iguales=[]
    mayores=[]

    for palabra in lista:
        if palabra<pivote:
            menores.append(palabra)
        elif palabra>pivote:
            mayores.append(palabra)
        else:
            iguales.append(palabra)

    return quick_sort(menores)+iguales+quick_sort(mayores)

# 4. Conteo de Frecuencia.
class TablaFrecuencias(TablaHashBase):
    def insertar(self, palabra):
        # Sobrescribimos el método insertar para guardar tuplas de (palabra, frecuencia)
        indice = self._hash(palabra)
        bucket = self.buckets[indice]

        for i, tupla in enumerate(bucket):
            p, freq = tupla
            if p == palabra:
                # Si ya existe, actualizamos su frecuencia sumando 1
                bucket[i] = (p, freq + 1)
                return
        
        # Si es una palabra nueva, la agregamos con frecuencia inicial de 1
        bucket.append((palabra, 1))

    def obtener_solo_palabras(self):
        # Sobrescribimos el método para extraer solo el texto de las tuplas
        resultado = []
        for bucket in self.buckets:
            for p, freq in bucket:
                resultado.append(p)
        return resultado

    def obtener_frecuencia(self, palabra):
        # Método exclusivo para consultar cuántas veces apareció una palabra
        indice = self._hash(palabra)
        for p, freq in self.buckets[indice]:
            if p == palabra:
                return freq
        return 0


# 5. Comparación empírica.

        
        
