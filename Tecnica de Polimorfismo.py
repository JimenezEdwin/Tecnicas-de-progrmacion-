#Tecnica de Polimorfismo
#Ejemplo de Gráfico de Figuras Geométricas

# Clase Base
class Figura:
    def dibujar(self):
        raise NotImplementedError("Cada figura debe saber cómo dibujarse.")

# Subclase 1
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
        
    # Implementación polimórfica de dibujar()
    def dibujar(self):
        print(f"Dibujando un Círculo con radio {self.radio}.")

# Subclase 2
class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        
    # Implementación polimórfica de dibujar()
    def dibujar(self):
        print(f"Dibujando un Rectángulo de {self.ancho}x{self.alto}.")

# Uso de Polimorfismo: Función que itera sobre cualquier objeto Figura
def renderizar_graficos(figuras):
    print("\n--- Renderizando Gráficos ---")
    for figura in figuras:
        # Llama al mismo método, pero cada objeto lo ejecuta a su manera
        figura.dibujar() 

# Lista de objetos de diferentes tipos
lista_de_figuras = [
    Circulo(7),
    Rectangulo(15, 30),
    Circulo(6)
]

renderizar_graficos(lista_de_figuras)
