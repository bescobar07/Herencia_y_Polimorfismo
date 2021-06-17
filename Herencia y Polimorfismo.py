class Persona():
    def __init__(self, nombres, apellidos, cedula, correo_personal, telefono, direccion):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.correo_personal = correo_personal
        self.telefono = telefono
        self.direccion = direccion

    def presentar(self):
        presentacion = (
            "\n\n\n\n se muestra los siguientes datos: Nombres: {}   Apellidos: {}   Cédula: {}  Correo Personal: {}  telefono: {}  direccion:{}")
        print(presentacion.format(self.nombres, self.apellidos, self.cedula, self.correo_personal, self.telefono,
                                  self.direccion))


class Estudiante(Persona):
    def __init__(self, nombres, apellidos, cedula, correo_personal, telefono, direccion):
        super().__init__(nombres, apellidos, cedula, correo_personal, telefono, direccion)


class Docente(Persona):
    def __init__(self, nombres, apellidos, cedula, correo_personal, telefono, direccion):
        super().__init__(nombres, apellidos, cedula, correo_personal, telefono, direccion)


class Administrativo(Persona):
    def __init__(self, nombres, apellidos, cedula, correo_personal, telefono, direccion):
        super().__init__(nombres, apellidos, cedula, correo_personal, telefono, direccion)


if __name__ == "main":
    objEstudiante = Estudiante("Byron Escobar", "Ing. Software")
    Estudiante.presentar()
    objdocente = Docente("Daniel Paredes Vera", "Ingeniera")
    Estudiante.presentar()
    objadministrativo = Administrativo("Richard Ramirez", "Rector")
    Estudiante.presentar()
    Docente.presentar()
    Administrativo.presentar()