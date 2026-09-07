# 2. Aseguradora
# 1. Validación Robusta

# Excepciones
class EdadInvalidaError(Exception):
    def __init__(self, mensaje="La edad debe ser entre 18 y 99 años."):
        super().__init__(mensaje)


class SexoInvalidoError(Exception):
    def __init__(self, mensaje="El sexo debe ser 'M' o 'F'."):
        super().__init__(mensaje)


class SumaAseguradaInvalidaError(Exception):
    def __init__(self, mensaje="La suma asegurada debe estar entre $500,000 y $3,000,000 MXN."):
        super().__init__(mensaje)


class OpcionInvalidaError(Exception):
    def __init__(self, mensaje="La opción ingresada debe ser 'Si' o 'No'."):
        super().__init__(mensaje)


# Clase para capturar y validar los datos del asegurado
class Datos:

    def ingresar_edad(self):
        while True:
            try:
                edad = int(input("Ingresa la edad del asegurado (18-99): "))
                if edad < 18 or edad > 99:
                    raise EdadInvalidaError()
                return edad
            except ValueError:
                print("Ingresa un número entero válido para la edad.\n")
            except EdadInvalidaError as error:
                print(f"Intente de nuevo. {error}\n")

    def ingresar_sexo(self):
        while True:
            try:
                sexo = input("Ingresa el sexo del asegurado (M ó F): ").strip().upper()
                if sexo not in ['M', 'F']:
                    raise SexoInvalidoError()
                return sexo
            except SexoInvalidoError as error:
                print(f"Intente de nuevo. {error}\n")

    def ingresar_suma_asegurada(self):
        while True:
            try:
                suma = float(input("Ingresa el monto de la suma asegurada ($500,000 - $3,000,000): "))
                if suma < 500000 or suma > 3000000:
                    raise SumaAseguradaInvalidaError()
                return suma
            except ValueError:
                print("Ingrese un monto numérico válido sin letras ni símbolos (Ej. 657987.89).\n")
            except SumaAseguradaInvalidaError as error:
                print(f"Intente de nuevo. {error}\n")

    def ingresar_opcion(self, pregunta):
        while True:
            try:
                respuesta = input(pregunta).strip().capitalize()
                if respuesta not in ['Si', 'No', 'Sí']:
                    raise OpcionInvalidaError()
                return respuesta
            except OpcionInvalidaError as error:
                print(f"Intente de nuevo. {error}\n")

    def recolectar_datos(self):
        print("Captura de datos del asegurado")
        edad = self.ingresar_edad()
        sexo = self.ingresar_sexo()
        suma = self.ingresar_suma_asegurada()
        fumador = self.ingresar_opcion("¿El asegurado es fumador? (Si/No): ")
        extra_prima = self.ingresar_opcion("¿El asegurado tiene extra prima? (Si/No): ")

        return {
            "edad": edad,
            "sexo": sexo,
            "suma_asegurada": suma,
            "fumador": fumador,
            "extra_prima": extra_prima
        }


# Programa
if __name__ == "__main__":
    capturador = Datos()
    cliente = capturador.recolectar_datos()

    print("Los datos han sido capturados.")
    print(cliente)
