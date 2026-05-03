# Importamos librerías necesarias
from abc import ABC, abstractmethod
from datetime import datetime


# Función para guardar errores y eventos
def registrar_log(mensaje):
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{datetime.now()} - {mensaje}\n")


# Excepción para cliente
class ClienteError(Exception):
    pass


# Excepción para servicio
class ServicioError(Exception):
    pass


# Excepción para reserva
class ReservaError(Exception):
    pass


# Clase abstracta general
class Persona(ABC):

    # Constructor
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    # Método obligatorio
    @abstractmethod
    def mostrar_datos(self):
        pass


# Clase cliente
class Cliente(Persona):

    # Constructor
    def __init__(self, nombre, documento, correo):
        super().__init__(nombre, documento)

        if nombre.strip() == "":
            raise ClienteError("Nombre vacío")

        if not documento.isdigit():
            raise ClienteError("Documento inválido")

        if "@" not in correo:
            raise ClienteError("Correo inválido")

        self.__correo = correo

    # Mostrar datos
    def mostrar_datos(self):
        return f"{self.nombre} - {self.documento} - {self.__correo}"

    # Obtener correo
    def get_correo(self):
        return self.__correo


# Clase abstracta servicio
class Servicio(ABC):

    # Constructor
    def __init__(self, nombre):
        self.nombre = nombre

    # Método obligatorio costo
    @abstractmethod
    def calcular_costo(self, descuento=0, impuesto=0):
        pass

    # Método obligatorio descripción
    @abstractmethod
    def descripcion(self):
        pass


# Servicio reserva sala
class ReservaSala(Servicio):

    # Constructor
    def __init__(self, horas):
        super().__init__("Reserva Sala")

        if horas <= 0:
            raise ServicioError("Horas inválidas")

        self.horas = horas

    # Calcular costo
    def calcular_costo(self, descuento=0, impuesto=0):
        total = self.horas * 50000
        total = total - (total * descuento / 100)
        total = total + (total * impuesto / 100)
        return total

    # Descripción
    def descripcion(self):
        return f"Sala por {self.horas} horas"


# Servicio alquiler equipo
class AlquilerEquipo(Servicio):

    # Constructor
    def __init__(self, dias):
        super().__init__("Alquiler Equipo")

        if dias <= 0:
            raise ServicioError("Días inválidos")

        self.dias = dias

    # Calcular costo
    def calcular_costo(self, descuento=0, impuesto=0):
        total = self.dias * 70000
        total = total - (total * descuento / 100)
        total = total + (total * impuesto / 100)
        return total

    # Descripción
    def descripcion(self):
        return f"Equipo por {self.dias} días"


# Servicio asesoría
class AsesoriaEspecializada(Servicio):

    # Constructor
    def __init__(self, horas):
        super().__init__("Asesoría")

        if horas <= 0:
            raise ServicioError("Horas inválidas")

        self.horas = horas

    # Calcular costo
    def calcular_costo(self, descuento=0, impuesto=0):
        total = self.horas * 90000
        total = total - (total * descuento / 100)
        total = total + (total * impuesto / 100)
        return total

    # Descripción
    def descripcion(self):
        return f"Asesoría por {self.horas} horas"


# Clase reserva
class Reserva:

    # Constructor
    def __init__(self, cliente, servicio):

        if not isinstance(cliente, Cliente):
            raise ReservaError("Cliente inválido")

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
            total = self.servicio.calcular_costo()
            self.confirmar()

        except Exception as error:
            raise ReservaError("Error procesando reserva") from error

        else:
            return total

        finally:
            registrar_log("Proceso terminado")

    # Mostrar reserva
    def mostrar(self):
        return f"""
Cliente: {self.cliente.nombre}
Servicio: {self.servicio.nombre}
Estado: {self.estado}
Costo: ${self.servicio.calcular_costo():,.0f}
"""


# Listas internas
clientes = []
reservas = []


# Registrar cliente
def registrar_cliente():
    try:
        nombre = input("Nombre: ")
        documento = input("Documento: ")
        correo = input("Correo: ")

        nuevo = Cliente(nombre, documento, correo)
        clientes.append(nuevo)

        print("Cliente registrado correctamente")

    except Exception as error:
        print("Error:", error)
        registrar_log(error)


# Ver clientes
def ver_clientes():
    if len(clientes) == 0:
        print("No hay clientes")

    else:
        for i, cliente in enumerate(clientes):
            print(i + 1, cliente.mostrar_datos())


# Crear reserva
def crear_reserva():
    try:
        if len(clientes) == 0:
            print("Primero registre clientes")
            return

        ver_clientes()
        opcion = int(input("Seleccione cliente: "))
        cliente = clientes[opcion - 1]

        print("1 Reserva Sala")
        print("2 Alquiler Equipo")
        print("3 Asesoría")

        tipo = int(input("Servicio: "))

        if tipo == 1:
            horas = int(input("Horas: "))
            servicio = ReservaSala(horas)

        elif tipo == 2:
            dias = int(input("Días: "))
            servicio = AlquilerEquipo(dias)

        elif tipo == 3:
            horas = int(input("Horas: "))
            servicio = AsesoriaEspecializada(horas)

        else:
            raise ServicioError("Servicio inválido")

        nueva = Reserva(cliente, servicio)
        nueva.procesar()
        reservas.append(nueva)

        print("Reserva creada correctamente")

    except Exception as error:
        print("Error:", error)
        registrar_log(error)


# Ver reservas
def ver_reservas():
    if len(reservas) == 0:
        print("No hay reservas")

    else:
        for reserva in reservas:
            print(reserva.mostrar())


# Cancelar reserva
def cancelar_reserva():
    try:
        if len(reservas) == 0:
            print("No existen reservas")
            return

        for i, reserva in enumerate(reservas):
            print(i + 1, reserva.cliente.nombre, reserva.estado)

        opcion = int(input("Seleccione reserva: "))
        reservas[opcion - 1].cancelar()

        print("Reserva cancelada")

    except Exception as error:
        print("Error:", error)
        registrar_log(error)


# Menú principal
while True:

    print("\nSOFTWARE FJ")
    print("1 Registrar cliente")
    print("2 Ver clientes")
    print("3 Crear reserva")
    print("4 Ver reservas")
    print("5 Cancelar reserva")
    print("6 Salir")

    try:
        opcion = int(input("Seleccione opción: "))

        if opcion == 1:
            registrar_cliente()

        elif opcion == 2:
            ver_clientes()

        elif opcion == 3:
            crear_reserva()

        elif opcion == 4:
            ver_reservas()

        elif opcion == 5:
            cancelar_reserva()

        elif opcion == 6:
            print("Sistema finalizado")
            break

        else:
            print("Opción inválida")

    except Exception as error:
        print("Error:", error)
        registrar_log(error)
