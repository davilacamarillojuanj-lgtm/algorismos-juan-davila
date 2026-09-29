"""Detección educativa de señales de fraude en transacciones.
Autor: Juan Davila Camarillo

No reemplaza los controles antifraude de una entidad financiera.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Transaccion:
    monto: float
    pais: str
    dispositivo_conocido: bool
    hora: int
    intentos_fallidos: int = 0


def evaluar_riesgo(transaccion: Transaccion) -> tuple[int, List[str]]:
    """Devuelve una puntuación de 0 a 100 y las señales encontradas."""
    puntuacion = 0
    señales: List[str] = []

    if transaccion.monto <= 0:
        raise ValueError("El monto debe ser mayor que cero")
    if transaccion.monto >= 5000:
        puntuacion += 25
        señales.append("monto elevado")
    if not transaccion.dispositivo_conocido:
        puntuacion += 30
        señales.append("dispositivo no reconocido")
    if transaccion.hora < 6 or transaccion.hora >= 23:
        puntuacion += 15
        señales.append("horario inusual")
    if transaccion.intentos_fallidos >= 3:
        puntuacion += 30
        señales.append("varios intentos fallidos")

    return min(puntuacion, 100), señales


if __name__ == "__main__":
    ejemplo = Transaccion(6500, "MX", False, datetime.now().hour, 3)
    riesgo, señales = evaluar_riesgo(ejemplo)
    print({"riesgo": riesgo, "señales": señales})
