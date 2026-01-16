# Paradigma Orientado a Objetos
# Se basa en clases, objetos y encapsulación

class SistemaSaludo:
    def __init__(self, usuario):
        self.usuario = usuario

    def ejecutar_saludo(self):
        print(f"Hola Mundo desde POO para: {self.usuario}")

# Instanciación del objeto
if __name__ == "__main__":
    mi_sistema = SistemaSaludo("Alumno de Python")
    mi_sistema.ejecutar_saludo()
