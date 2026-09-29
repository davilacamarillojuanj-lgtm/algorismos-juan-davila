"""
Algoritmo de Gestión Financiera Personal
Propietario: Juan Davila Camarillo
RFC: DACJ871001KTA
Autor: Juan Davila Camarillo
Fecha: 2026-09-29

Sistema de control y análisis de finanzas personales.
"""

from datetime import datetime
from typing import List, Dict
from dataclasses import dataclass


@dataclass
class Ingreso:
    """Representa un ingreso mensual."""
    concepto: str
    monto: float
    fecha: datetime


@dataclass
class Gasto:
    """Representa un gasto realizado."""
    categoria: str
    descripcion: str
    monto: float
    fecha: datetime


class GestorFinanzasJuan:
    """Gestor financiero personal para Juan Davila Camarillo (RFC: DACJ871001KTA)."""
    
    def __init__(self):
        self.ingresos: List[Ingreso] = []
        self.gastos: List[Gasto] = []
        self.propietario = "Juan Davila Camarillo"
        self.rfc = "DACJ871001KTA"
        
    def agregar_ingreso(self, concepto: str, monto: float) -> Dict:
        """Registra un nuevo ingreso."""
        ingreso = Ingreso(
            concepto=concepto,
            monto=monto,
            fecha=datetime.now()
        )
        self.ingresos.append(ingreso)
        return {
            "estado": "ingreso registrado",
            "concepto": concepto,
            "monto": monto,
            "propietario": self.propietario,
            "rfc": self.rfc
        }
    
    def agregar_gasto(self, categoria: str, descripcion: str, monto: float) -> Dict:
        """Registra un nuevo gasto."""
        gasto = Gasto(
            categoria=categoria,
            descripcion=descripcion,
            monto=monto,
            fecha=datetime.now()
        )
        self.gastos.append(gasto)
        return {
            "estado": "gasto registrado",
            "categoria": categoria,
            "descripcion": descripcion,
            "monto": monto,
            "propietario": self.propietario,
            "rfc": self.rfc
        }
    
    def calcular_balance(self) -> Dict:
        """Calcula el balance total de ingresos y gastos."""
        total_ingresos = sum(i.monto for i in self.ingresos)
        total_gastos = sum(g.monto for g in self.gastos)
        balance = total_ingresos - total_gastos
        
        return {
            "propietario": self.propietario,
            "rfc": self.rfc,
            "total_ingresos": total_ingresos,
            "total_gastos": total_gastos,
            "balance_neto": balance,
            "estado": "positivo" if balance >= 0 else "negativo"
        }
    
    def obtener_resumen(self) -> Dict:
        """Genera un resumen completo de finanzas."""
        balance = self.calcular_balance()
        
        gastos_por_categoria = {}
        for gasto in self.gastos:
            if gasto.categoria not in gastos_por_categoria:
                gastos_por_categoria[gasto.categoria] = 0
            gastos_por_categoria[gasto.categoria] += gasto.monto
        
        return {
            "propietario": self.propietario,
            "rfc": self.rfc,
            "fecha_reporte": datetime.now().isoformat(),
            "total_ingresos": balance["total_ingresos"],
            "total_gastos": balance["total_gastos"],
            "balance_neto": balance["balance_neto"],
            "gastos_por_categoria": gastos_por_categoria,
            "numero_ingresos": len(self.ingresos),
            "numero_gastos": len(self.gastos)
        }


if __name__ == "__main__":
    # Ejemplo de uso para Juan Davila Camarillo
    gestor = GestorFinanzasJuan()
    
    print("=" * 60)
    print(f"GESTOR FINANCIERO PERSONAL")
    print(f"Propietario: {gestor.propietario}")
    print(f"RFC: {gestor.rfc}")
    print("=" * 60)
    print()
    
    # Registrar ingresos
    print("Registrando ingresos...")
    gestor.agregar_ingreso("Salario", 15000)
    gestor.agregar_ingreso("Freelance", 3000)
    print("✓ Ingresos registrados")
    print()
    
    # Registrar gastos
    print("Registrando gastos...")
    gestor.agregar_gasto("Vivienda", "Renta", 5000)
    gestor.agregar_gasto("Alimentación", "Supermercado", 1200)
    gestor.agregar_gasto("Transporte", "Gasolina", 800)
    gestor.agregar_gasto("Entretenimiento", "Cine y otros", 500)
    print("✓ Gastos registrados")
    print()
    
    # Mostrar resumen
    resumen = gestor.obtener_resumen()
    print("RESUMEN FINANCIERO")
    print("-" * 60)
    for clave, valor in resumen.items():
        print(f"{clave}: {valor}")
