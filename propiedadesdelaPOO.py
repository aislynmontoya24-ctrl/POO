# ------- Clase que representa una propiedad de POO ---------

class PropiedadPOO:
    def _init_(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def mostrar(self):
        print(f"\n📘 {self.nombre}")
        print(self.descripcion)


# --------- Clase Evaluación -------------

class Evaluacion:
    def _init_(self):
        self.preguntas = [
            {
                "pregunta": "1. ¿Qué propiedad de POO permite que una clase herede atributos y métodos?\n"
                            "a) Encapsulamiento\nb) Herencia\nc) Polimorfismo",
                "respuesta": "b"
            },
            {
                "pregunta": "2. ¿Qué propiedad permite que varios objetos usen el mismo método pero con comportamiento distinto?\n"
                            "a) Polimorfismo\nb) Abstracción\nc) Herencia",
                "respuesta": "a"
            },
            {
                "pregunta": "3. ¿Qué propiedad oculta detalles internos para mostrar solo lo esencial?\n"
                            "a) Abstracción\nb) Encapsulamiento\nc) Polimorfismo",
                "respuesta": "a"
            },
            {
                "pregunta": "4. ¿Qué propiedad controla el acceso a los datos internos de un objeto?\n"
                            "a) Encapsulamiento\nb) Herencia\nc) Abstracción",
                "respuesta": "a"
            },
        ]

    def aplicar(self):
        print("\n📝 INICIA LA EVALUACIÓN\nEscribe solo la letra de tu respuesta.")
        correctas = 0

        for p in self.preguntas:
            print("\n" + p["pregunta"])
            r = input("Respuesta: ").lower()

            if r == p["respuesta"]:
                print("✔ Correcto")
                correctas += 1
            else:
                print("✘ Incorrecto")

        print(f"\nTu calificación final es: {correctas}/{len(self.preguntas)}")


# ------------- Programa principal -----------------

def main():
    propiedades = [
        PropiedadPOO("Encapsulamiento", 
                     "Consiste en ocultar los datos internos de un objeto y controlar su acceso."),
        PropiedadPOO("Herencia",
                     "Permite crear nuevas clases a partir de una clase existente."),
        PropiedadPOO("Polimorfismo",
                     "Permite que un mismo método se comporte de manera diferente según el objeto."),
        PropiedadPOO("Abstracción",
                     "Consiste en mostrar solo los aspectos esenciales y ocultar los detalles."),
    ]

    evaluacion = Evaluacion()

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ver propiedades de POO")
        print("2. Tomar evaluación")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            for p in propiedades:
                p.mostrar()

        elif opcion == "2":
            evaluacion.aplicar()

        elif opcion == "3":
            print("¡Hasta luego! 👋")
            break
        else:
            print("Opción inválida.")


# Ejecutar programa
if _name_ == "_main_":
    main()