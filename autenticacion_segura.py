"""Autenticación educativa con hash PBKDF2 y tokens HMAC.

No almacena contraseñas en texto plano. En producción usa un proveedor
especializado de identidad y controles como MFA, bloqueo progresivo y auditoría.
"""
import hashlib
import hmac
import secrets
from typing import Tuple

ITERACIONES = 600_000


def crear_credencial(password: str) -> Tuple[str, str]:
    if len(password) < 12:
        raise ValueError("La contraseña debe tener al menos 12 caracteres")
    sal = secrets.token_bytes(16)
    derivada = hashlib.pbkdf2_hmac("sha256", password.encode(), sal, ITERACIONES)
    return sal.hex(), derivada.hex()


def verificar_password(password: str, sal_hex: str, hash_hex: str) -> bool:
    sal = bytes.fromhex(sal_hex)
    esperada = hashlib.pbkdf2_hmac(
        "sha256", password.encode(), sal, ITERACIONES
    ).hex()
    return hmac.compare_digest(esperada, hash_hex)


def crear_token() -> str:
    return secrets.token_urlsafe(32)


if __name__ == "__main__":
    sal, hash_password = crear_credencial("Una contraseña segura 2026!")
    print("¿Contraseña válida?", verificar_password("Una contraseña segura 2026!", sal, hash_password))
    print("Token de sesión de ejemplo:", crear_token())
