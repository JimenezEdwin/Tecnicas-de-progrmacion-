#Tecnica de encapsulación
#Ejemplo de la configuracion de la temperatura

class Termostato:
    def __init__(self, temp_inicial=20):
        # Atributo privado y encapsulado
        self.__temperatura_celsius = temp_inicial
    
    # Getter (Método de acceso)
    def obtener_temperatura(self):
        return self.__temperatura_celsius
    
    # Setter (Método de modificación) con validación
    def establecer_temperatura(self, nueva_temp):
        if 15 <= nueva_temp <= 30: # Regla de negocio: rango válido
            self.__temperatura_celsius = nueva_temp
            print(f"Temperatura establecida a {nueva_temp}°C.")
        else:
            print(f"Error: {nueva_temp}°C está fuera del rango permitido (15°C - 30°C).")

# Uso (Acceso y modificación controlados):
climatizador = Termostato()
print(f"Temperatura actual: {climatizador.obtener_temperatura()}°C")

# Modificación válida (a través del setter)
climatizador.establecer_temperatura(24) 

# Modificación inválida (el setter impide el cambio)
climatizador.establecer_temperatura(54) 

# Intentar acceder o modificar el atributo privado directamente (desaconsejado/complicado)
# print(climatizador.__temperatura_celsius)