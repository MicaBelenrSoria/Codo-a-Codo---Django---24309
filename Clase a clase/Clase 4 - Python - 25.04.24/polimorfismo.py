class Circulo:
    def dibujar(self):
        print("0")


class Rectangulo:
    def dibujar(self):
        print("#")


class Triangulo:
    def dibujar(self):
        print("$")

figuras = [Circulo(), Rectangulo(), Triangulo()]

for figura in figuras:
    figura.dibujar()

a = 4; b = 0
print("Haciendo cuenta")
print(a/b)
print("Cuenta hecha")