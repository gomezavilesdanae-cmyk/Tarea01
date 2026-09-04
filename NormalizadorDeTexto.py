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
