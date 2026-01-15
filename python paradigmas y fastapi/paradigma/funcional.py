# Paradigma Funcional
# Se basa en funciones puras y funciones de orden superior

# Función pura (no modifica estado externo)
obtener_saludo = lambda nombre: f"Hola Mundo Funcional, {nombre}"

# Función de orden superior
def presentador(funcion_logica, nombre_usuario):
    mensaje = funcion_logica(nombre_usuario)
    print(mensaje)

# Punto de entrada del programa
if __name__ == "__main__":
    presentador(obtener_saludo, "Alumno")
