#Tecnica de Herencia
#Ejemplo de tipos de empleados

# Superclase
class Empleado:
    def __init__(self, nombre, id_empleado):
        self.nombre = nombre
        self.id_empleado = id_empleado
    
    def trabajar(self):
        return f"{self.nombre} está realizando tareas genéricas de oficina."

# Subclase 1
class Desarrollador(Empleado):
    def __init__(self, nombre, id_empleado, lenguaje):
        super().__init__(nombre, id_empleado)
        self.lenguaje = lenguaje
        
    # Sobreescritura del método trabajar para hacerlo específico
    def trabajar(self):
        return f"{self.nombre} (ID: {self.id_empleado}) está programando en {self.lenguaje}."

# Subclase 2
class Gerente(Empleado):
    # El gerente solo necesita el constructor heredado
    
    # Nuevo método específico
    def organizar_equipo(self):
        return f"{self.nombre} está organizando las tareas del equipo."

# Uso:
dev = Desarrollador("Edwin", "D1722", "Python")
manager = Gerente("Xavier", "G332")

print(f"Desarrollador: {dev.trabajar()}") # Método sobrescrito
print(f"Gerente: {manager.trabajar()}")   # Método heredado
print(f"Gerente: {manager.organizar_equipo()}") # Método propio