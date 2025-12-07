Tecnica de Abstracion
Ejemplo de un sistema de pago

from abc import ABC, abstractmethod

# Clase Abstracta
class MetodoPago(ABC):
    """Define la interfaz esencial para cualquier método de pago."""
    
    @abstractmethod
    def procesar_pago(self, monto):
        pass

# Implementación concreta 1: Oculta los detalles de la tarjeta de crédito
class PagoTarjetaCredito(MetodoPago):
    def __init__(self, numero, cvc):
        self._numero = numero  # Detalle oculto (protegido)
        self._cvc = cvc        # Detalle oculto (protegido)

    def procesar_pago(self, monto):
        # Lógica compleja de comunicación con el banco (detalle oculto)
        print(f"Procesando pago con Tarjeta de Crédito por ${monto}.")
        print("Verificando credenciales bancarias...")
        return True

# Implementación concreta 2: Oculta los detalles de la transferencia bancaria
class PagoTransferencia(MetodoPago):
    def procesar_pago(self, monto):
        # Lógica compleja de autenticación y transferencia (detalle oculto)
        print(f"Procesando transferencia bancaria por ${monto}.")
        print("Generando código de confirmación...")
        return True

# Uso abstracto (el código solo sabe que tiene un 'MetodoPago')
tarjeta = PagoTarjetaCredito("1234...", "000")
transferencia = PagoTransferencia()

print("\n--- Tienda Virtual ---")
tarjeta.procesar_pago(99.50)
transferencia.procesar_pago(45.00)