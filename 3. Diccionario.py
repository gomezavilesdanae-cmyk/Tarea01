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


# 2. Eliminación de repetidos con tabla hash propia y 4. Conteo de frecuencia
class TablaHashDiccionario:
    def __init__(self, tamano=100):
        self.tamano = tamano
        # Buckets (listas) para manejar colisiones por encadenamiento
        self.buckets = [[] for _ in range(self.tamano)]

    def _hash(self, palabra):
        suma = sum(ord(c) for c in palabra)
        return suma % self.tamano

    def insertar(self, palabra):
        indice = self._hash(palabra)
        bucket = self.buckets[indice]

        for i, (p, freq) in enumerate(bucket):
            if p == palabra:
                bucket[i] = (p, freq + 1)
                return
        
        bucket.append((palabra, 1))

    # Nuevo método para consultar frecuencias fácilmente
    def obtener_frecuencia(self, palabra):
        indice = self._hash(palabra)
        for p, freq in self.buckets[indice]:
            if p == palabra:
                return freq
        return 0

    def obtener_solo_palabras(self):
        resultado = []
        for bucket in self.buckets:
            for p, freq in bucket:
                resultado.append(p)
        return resultado

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

        
        
