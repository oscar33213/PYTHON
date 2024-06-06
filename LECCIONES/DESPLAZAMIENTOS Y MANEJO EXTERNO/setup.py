from setuptools import setup, find_packages # type: ignore

setup(
    name="Paquete Oscar",
    version="1.0.0",  # Corregido el número de versión
    description="Paquete de prueba personal",
    long_description="Paquete de prueba personal para curso",
    author="Oscar Hidalgo",
    author_email="oshill463@gmail.com",
    packages=find_packages(include=["MIPAQUETE", "NUMDOS"]),  # Corregido los nombres de los paquetes
)
