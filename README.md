# Python: Paradigmas de Programación y FastAPI

## Descripción
Este repositorio presenta la administración de entornos de desarrollo
locales y en la nube, así como la implementación de tres paradigmas de
programación en Python: funcional, orientado a objetos y orientado a
datos. Además, se incluye una API básica desarrollada con FastAPI.

## Entornos de desarrollo
- VS Code (entorno local)
- Anaconda / Jupyter (opcional para documentación)
- GitHub Codespaces (entorno en la nube)

## Estructura del proyecto
- fastapi_app/main.py → API básica con FastAPI
- paradigma/funcional.py → Programación Funcional
- paradigma/poo.py → Programación Orientada a Objetos
- paradigma/pod.py → Programación Orientada a Datos

## Ejecución del proyecto

### FastAPI
```bash
uvicorn fastapi_app.main:app --reload
