"""Validación de datos de transferencias antes de procesarlas."""
import re
from decimal import Decimal, InvalidOperation
from typing import Dict, List

CLABE = re.compile(r"^\d{18}$")


def validar_transferencia(datos: Dict[str, str]) -> List[str]:
    errores: List[str] = []
    cuenta = datos.get("cuenta_destino", "").replace(" ", "")
    concepto = datos.get("concepto", "").strip()

    if not CLABE.fullmatch(cuenta):
        errores.append("La cuenta destino debe contener 18 dígitos")
    try:
        monto = Decimal(datos.get("monto", ""))
        if monto <= 0 or monto > Decimal("500000"):
            errores.append("El monto debe estar entre 0 y 500000")
    except InvalidOperation:
        errores.append("El monto no es válido")
    if len(concepto) > 40:
        errores.append("El concepto no puede superar 40 caracteres")
    if any(ord(caracter) < 32 for caracter in concepto):
        errores.append("El concepto contiene caracteres no permitidos")

    return errores


if __name__ == "__main__":
    solicitud = {"cuenta_destino": "646180157812345678", "monto": "250.00", "concepto": "Pago de servicio"}
    print("Transferencia válida" if not validar_transferencia(solicitud) else validar_transferencia(solicitud))
