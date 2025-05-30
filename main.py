from datetime import date

class Beneficiario:
    def __init__(self, nombre, documento, edad, poblacion_vulnerable):
        self.nombre = nombre
        self.documento = documento
        self.edad = edad
        self.poblacion_vulnerable = poblacion_vulnerable
        self.asistencias = []

    def registrar_asistencia(self, fecha):
        if fecha not in self.asistencias:
            self.asistencias.append(fecha)

    def __str__(self):
        return f"{self.nombre} ({self.documento})"


class Comedor:
    def __init__(self, nombre, cupos_diarios):
        self.nombre = nombre
        self.cupos_diarios = cupos_diarios
        self.beneficiarios_asignados = []

    def asignar_beneficiario(self, beneficiario):
        if len(self.beneficiarios_asignados) < self.cupos_diarios:
            self.beneficiarios_asignados.append(beneficiario)
            return True
        return False

    def listado_diario(self):
        return [str(b) for b in self.beneficiarios_asignados]


class SistemaComedor:
    def __init__(self):
        self.beneficiarios = {}
        self.comedores = {}

    def registrar_beneficiario(self):
        nombre = input("Nombre: ")
        documento = input("Documento: ")
        if documento in self.beneficiarios:
            print("Beneficiario ya registrado.")
            return
        edad = int(input("Edad: "))
        poblacion_vulnerable = input("Población vulnerable (sí/no): ").lower() == "sí"
        self.beneficiarios[documento] = Beneficiario(nombre, documento, edad, poblacion_vulnerable)
        print("Beneficiario registrado.")

    def registrar_comedor(self):
        nombre = input("Nombre del comedor: ")
        if nombre in self.comedores:
            print("Comedor ya registrado.")
            return
        cupos = int(input("Cupos diarios: "))
        self.comedores[nombre] = Comedor(nombre, cupos)
        print("Comedor registrado.")

    def asignar_cupo(self):
        doc = input("Documento del beneficiario: ")
        if doc not in self.beneficiarios:
            print("Beneficiario no encontrado.")
            return
        comedor_nombre = input("Nombre del comedor: ")
        if comedor_nombre not in self.comedores:
            print("Comedor no encontrado.")
            return
        comedor = self.comedores[comedor_nombre]
        beneficiario = self.beneficiarios[doc]
        if comedor.asignar_beneficiario(beneficiario):
            print("Cupo asignado.")
        else:
            print("No hay cupos disponibles.")

    def registrar_asistencia(self):
        doc = input("Documento del beneficiario: ")
        if doc in self.beneficiarios:
            self.beneficiarios[doc].registrar_asistencia(str(date.today()))
            print("Asistencia registrada.")
        else:
            print("Beneficiario no encontrado.")

    def generar_reporte_diario(self):
        comedor_nombre = input("Nombre del comedor: ")
        if comedor_nombre not in self.comedores:
            print("Comedor no encontrado.")
            return
        print(f"\nListado diario de {comedor_nombre}:")
        for b in self.comedores[comedor_nombre].listado_diario():
            print(f"- {b}")

    def menu(self):
        opciones = {
            "1": self.registrar_beneficiario,
            "2": self.registrar_comedor,
            "3": self.asignar_cupo,
            "4": self.registrar_asistencia,
            "5": self.generar_reporte_diario,
            "0": exit
        }
        while True:
            print("\n--- MENÚ ---")
            print("1. Registrar beneficiario")
            print("2. Registrar comedor")
            print("3. Asignar cupo")
            print("4. Registrar asistencia")
            print("5. Generar reporte diario")
            print("0. Salir")
            opcion = input("Seleccione una opción: ")
            accion = opciones.get(opcion)
            if accion:
                accion()
            else:
                print("Opción inválida.")

if __name__ == "__main__":
    sistema = SistemaComedor()
    sistema.menu()
