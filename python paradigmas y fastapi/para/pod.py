# Paradigma Orientado a Datos
# Se enfoca en la estructura del dato y su procesamiento

from dataclasses import dataclass

@dataclass
class DatosUsuario:
    nombre: str
    rol: str
    id_sesion: int

def imprimir_ficha(datos: DatosUsuario):
    print(f"Hola Mundo Data-Oriented: {datos.nombre} | Rol: {datos.rol}")

if __name__ == "__main__":
    usuario_actual = DatosUsuario(nombre="Alumno", rol="Admin", id_sesion=101)
    imprimir_ficha(usuario_actual)
