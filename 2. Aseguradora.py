from abc import ABC, abstractmethod

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

# Conversión de moneda 
# Principio: Single Resonsibility Principle (SRP) 
class TasaCambioInvalidaError(Exception):
    def __init__(self, mensaje="La tasa de cambio debe ser un número positivo mayor a cero"):
        super().__init__(mensaje)

class ConversorMoneda:
    """Clase independiente para manejar la conversión de divisas, desacoplada del cálculo de seguros."""
    def __init__(self, tasa_cambio: float = 21.13):
        if tasa_cambio <=0:
            raise TasaCambioInvalidaError()
        self.tasa_cambio = tasa_cambio 
    def mxn_a_usd(self, monto_mxn: float) -> float:
        return monto_mxn / self.tasa_cambio

# Jerarquía de clases para factor de edad
# Principio: Open/Closed Principle (OCP)
class FactorEdadStrategy (ABC):
    """Clase abstracta que define el contrato para obtener el factor de edad"""
    @abstractmethod 
    def obtener_factor(self, edad_ajustada: int) -> float:
        pass
        
class FactorFemenino(FactorEdadStrategy):
    def obtener_factor(self, edad_ajustada: int) -> float:
        if 18 <= edad_ajustada < 25:
            return 1.5 
        elif 25 <= edad_ajustada < 45:
            return 1.7 
        elif 45 <= edad_ajustada < 65:
            return 2.0
        elif 65 <= edad_ajustada <=99:
            return 2.2 
        return 1.5

class FactorMasculino(FactorEdadStrategy):
    def obtener_factor(self, edad_ajustada: int) -> float:
        if 18 <= edad_ajustada < 25:
            return 2.0 
        elif 25 <= edad_ajustada < 45:
            return 2.3
        elif 45 <= edad_ajustada < 65:
            return 2.5
        elif 65 <= edad_ajustada <=99:
            return 3.0 
        return 2.0

# Calculadora principal del seguro 
class CalculadoraSeguro:
    def __init__(self, conversor: ConversorMoneda = None):
        # Inyección de dependencias (Si no le pasamos conversor, crea uno por defecto)
        self.conversor = conversor if conversor else ConversorMoneda()
    def _calcular_edad_ajustada(self, edad: int, sexo: str, fumador: str, extra_prima: str):
        """Calcula la edad ajustada aplicando las reglas de negocio."""
        edad_ajustada = edad
        
        if fumador in ['No', 'NO']:
            edad_ajustada -= 5
        if sexo == 'F':
            edad_ajustada -= 10
        if extra_prima in ['Si', 'Sí', 'SI']:
            edad_ajustada += 10
            
        # Restricción: La edad ajustada nunca puede salir del rango [18, 99]
        return max(18, min(edad_ajustada, 99))
    def calcular_prima(self, datos_cliente: dict) -> dict:
        """Recibe el diccionario y devuelve los resultados"""
        # 1. Obtener la edad ajustada
        edad_ajustada = self._calcular_edad_ajustada(
            datos_cliente['edad'],
            datos_cliente['sexo'],
            datos_cliente['fumador'],
            datos_cliente['extra_prima']
        )
        
        # 2. Seleccionar la estrategia adecuada (Open/Closed)
        if datos_cliente['sexo'] == 'F':
            estrategia_factor = FactorFemenino()
        else:
            estrategia_factor = FactorMasculino()
            
        # 3. Obtener el factor K
        k = estrategia_factor.obtener_factor(edad_ajustada)
        
        # 4. Calcular Prima Anual: P = (SA * K) / 1000
        sa = datos_cliente['suma_asegurada']
        prima_mxn = (sa * k) / 1000
        
        # 5. Convertir a dólares usando la clase independiente
        prima_usd = self.conversor.mxn_a_usd(prima_mxn)
        
        return {
            "edad_original": datos_cliente['edad'],
            "edad_ajustada": edad_ajustada,
            "factor_k": k,
            "prima_mxn": round(prima_mxn, 2),
            "prima_usd": round(prima_usd, 2)
        }

# Programa principal
if __name__ == "__main__":
    
    #Entrada de datos
    capturador = Datos()
    calculadora = CalculadoraSeguro()
    asegurados = []
    primas = []
    n = int(input("¿Cuántos asegurados desea registrar?: "))
    
    # Procesamiento
    for i in range(n):
        print(f"\n--- Asegurado {i+1} ---")
        cliente_datos = capturador.recolectar_datos()
        resultados = calculadora.calcular_prima(cliente_datos)
        
        asegurados.append({
            "datos": clientes_datos,
            "resultados": resultados})
        primas.append(resultados["prima_mxn"])
        
    # Estadísticas
    promedio = sum(primas) / len(primas)
    maxima = max(primas)
    minima = min(primas)
    print("\n---Estadísticas---")
    print(f"Prima promedio: ${promedio:,.2f}")
    
        
    
