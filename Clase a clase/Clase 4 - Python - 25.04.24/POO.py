#El paradigma orientado a objetos es el que define los programas en termino de comunidades de objetos. Los objetos son caracteristicas comunes y se agrupan en clases  
#ES UNA FORMA DE VER EL MUNDO

class Alumno:
    def __init__(self,nombre, apellido, dni):
            self.nombre = nombre 
            self.apellido = apellido
            self.dni = dni

    def alta(self):
          print(f"F1 alumno {self.nombre} {self.apellido} se dio de alta el curso")

    def __eq__ (self, other):
        return self.dni == other.dni 


class Docente:
    def __init__ (self, dni):
         self.dni = dni

    def __eq__(self, other):
         return self.dni == other.dni


alumno1 = Alumno("Carlos", "Lopez", 1234)
alumno2 = Alumno("Maria", "Del Cerro", 5678)
alumno3 = Alumno("Gaston", "Perez", 1234)

docente1 = Docente(1234)

print(alumno1.nombre, alumno1.apellido)

alumno1.alta()
alumno2.alta()

print(alumno1 = alumno2)
print(alumno1 = alumno3)

print(alumno1 == docente1)