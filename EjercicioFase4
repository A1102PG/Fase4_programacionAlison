# Importamos herramientas necesarias
from abc import ABC, abstractmethod
from datetime import datetime


# Función para guardar eventos y errores en archivo de texto
def registrar_log(mensaje):
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{datetime.now()} - {mensaje}\n")


# Excepción personalizada para errores de cliente
class ClienteError(Exception):
    pass


# Excepción personalizada para errores de servicios
class ServicioError(Exception):
    pass


# Excepción personalizada para errores de reservas
class ReservaError(Exception):
    pass


# Clase abstracta general para personas
class Persona(ABC):

    # Constructor principal
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    # Método obligatorio para clases hijas
    @abstractmethod
    def mostrar_datos(self):
        pass


# Clase Cliente heredada de Persona
class Cliente(Persona):

    # Constructor del cliente
    def __init__(self, nombre, documento, correo):
        super().__init__(nombre, documento)

        # Validamos nombre vacío
        if nombre.strip() == "":
            raise ClienteError("El nombre no puede estar vacío")

        # Validamos documento numérico
        if not documento.isdigit():
            raise ClienteError("Documento inválido")

        # Validamos correo
        if "@" not in correo:
            raise ClienteError("Correo inválido")

        # Encapsulación del correo
        self.__correo = correo

    # Mostrar información del cliente
    def mostrar_datos(self):
        return f"Cliente: {self.nombre} - Documento: {self.documento}"

    # Obtener correo encapsulado
    def get_correo(self):
        return self.__correo


# Clase abstracta para servicios
class Servicio(ABC):

    # Constructor principal
    def __init__(self, nombre):
        self.nombre = nombre

    # Método obligatorio para calcular costo
    @abstractmethod
    def calcular_costo(self):
        pass

    # Método obligatorio para descripción
    @abstractmethod
    def descripcion(self):
        pass


# Servicio de reserva de sala
class ReservaSala(Servicio):

    # Constructor
    def __init__(self, horas):
        super().__init__("Reserva de Sala")

        # Validamos horas
        if horas <= 0:
            raise ServicioError("Horas inválidas")

        self.horas = horas

    # Calcular costo
    def calcular_costo(self):
        return self.horas * 50000

    # Descripción
    def descripcion(self):
        return f"Reserva de sala por {self.horas} horas"


# Servicio de alquiler de equipos
class AlquilerEquipo(Servicio):

    # Constructor
    def __init__(self, dias):
        super().__init__("Alquiler de Equipo")

        # Validamos días
        if dias <= 0:
            raise ServicioError("Días inválidos")

        self.dias = dias

    # Calcular costo
    def calcular_costo(self):
        return self.dias * 70000

    # Descripción
    def descripcion(self):
        return f"Alquiler de equipo por {self.dias} días"


# Servicio de asesoría especializada
class AsesoriaEspecializada(Servicio):

    # Constructor
    def __init__(self, horas):
        super().__init__("Asesoría Especializada")

        # Validamos horas
        if horas <= 0:
            raise ServicioError("Horas inválidas")

        self.horas = horas

    # Calcular costo
    def calcular_costo(self):
        return self.horas * 90000

    # Descripción
    def descripcion(self):
        return f"Asesoría especializada por {self.horas} horas"


# Clase para reservas
class Reserva:

    # Constructor
    def __init__(self, cliente, servicio):

        # Validamos cliente
        if not isinstance(cliente, Cliente):
            raise ReservaError("Cliente inválido")

        # Validamos servicio
        if not isinstance(servicio, Servicio):
            raise ReservaError("Servicio inválido")

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    # Confirmar reserva
    def confirmar(self):
        self.estado = "Confirmada"
        registrar_log("Reserva confirmada")

    # Cancelar reserva
    def cancelar(self):
        self.estado = "Cancelada"
        registrar_log("Reserva cancelada")

    # Procesar reserva
    def procesar(self):

        try:
            costo = self.servicio.calcular_costo()
            self.confirmar()

        except Exception as error:
            raise ReservaError("No fue posible procesar la reserva") from error

        else:
            return costo

        finally:
            registrar_log("Proceso finalizado")

    # Mostrar información
    def mostrar(self):
        return f"""
Cliente: {self.cliente.nombre}
Servicio: {self.servicio.nombre}
Estado: {self.estado}
Costo: ${self.servicio.calcular_costo():,.0f}
"""


# Inicio del sistema
print("===================================")
print(" SISTEMA SOFTWARE FJ ")
print("===================================\n")


# Operación 1 Cliente correcto
try:
    cliente1 = Cliente("Ana Puentes", "12345", "ana@gmail.com")
    print(cliente1.mostrar_datos())

except Exception as error:
    print(error)
    registrar_log(error)


# Operación 2 Cliente incorrecto
try:
    cliente2 = Cliente("", "ABC", "correo")

except Exception as error:
    print("Error:", error)
    registrar_log(error)


# Operación 3 Servicio correcto
try:
    servicio1 = ReservaSala(3)
    print(servicio1.descripcion())

except Exception as error:
    print(error)
    registrar_log(error)


# Operación 4 Servicio incorrecto
try:
    servicio2 = AlquilerEquipo(-5)

except Exception as error:
    print("Error:", error)
    registrar_log(error)


# Operación 5 Otro servicio correcto
try:
    servicio3 = AsesoriaEspecializada(2)
    print(servicio3.descripcion())

except Exception as error:
    print(error)
    registrar_log(error)


# Operación 6 Reserva exitosa
try:
    reserva1 = Reserva(cliente1, servicio1)
    reserva1.procesar()
    print(reserva1.mostrar())

except Exception as error:
    print(error)
    registrar_log(error)


# Operación 7 Segunda reserva
try:
    reserva2 = Reserva(cliente1, servicio3)
    reserva2.procesar()
    print(reserva2.mostrar())

except Exception as error:
    print(error)
    registrar_log(error)


# Operación 8 Reserva incorrecta
try:
    reserva3 = Reserva("cliente falso", servicio1)

except Exception as error:
    print("Error:", error)
    registrar_log(error)


# Operación 9 Cancelar reserva
try:
    reserva1.cancelar()
    print("Reserva cancelada correctamente")

except Exception as error:
    print(error)
    registrar_log(error)


# Operación 10 Nueva reserva
try:
    servicio4 = AlquilerEquipo(4)
    reserva4 = Reserva(cliente1, servicio4)
    reserva4.procesar()
    print(reserva4.mostrar())

except Exception as error:
    print(error)
    registrar_log(error)


# Mensaje final
print("Sistema ejecutado correctamente")
