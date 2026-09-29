"""Cifrado de archivos de demostración usando Fernet.

Instalación: pip install -r requirements.txt
Nunca guardes claves en el código ni las compartas.
"""
from cryptography.fernet import Fernet


def generar_clave() -> bytes:
    """Genera una clave nueva; guárdala de forma segura."""
    return Fernet.generate_key()


def cifrar(mensaje: str, clave: bytes) -> bytes:
    return Fernet(clave).encrypt(mensaje.encode("utf-8"))


def descifrar(datos: bytes, clave: bytes) -> str:
    return Fernet(clave).decrypt(datos).decode("utf-8")


if __name__ == "__main__":
    clave = generar_clave()
    secreto = cifrar("Datos de prueba", clave)
    print("Texto cifrado:", secreto.decode())
    print("Texto original:", descifrar(secreto, clave))
