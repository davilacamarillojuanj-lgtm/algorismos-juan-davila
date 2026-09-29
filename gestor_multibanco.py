"""
Gestor Multibanco - Integrador de BBVA y Santander
Propietario: Juan Davila Camarillo
RFC: DACJ871001KTA
Autor: Juan Davila Camarillo

Sistema que integra saldos y transacciones de múltiples bancos.
"""

import os
from typing import Dict, List
from datetime import datetime
from sistema_saldos_bbva import SistemaBalanceBBVA
from sistema_saldos_santander import SistemaBalanceSantander
from dotenv import load_dotenv

load_dotenv()


class GestorMultibanco:
    """Gestor que integra múltiples bancos en un solo dashboard."""
    
    def __init__(self):
        self.propietario = "Juan Davila Camarillo"
        self.rfc = "DACJ871001KTA"
        self.bbva = SistemaBalanceBBVA()
        self.santander = SistemaBalanceSantander()
        self.saldos_totales_cache = {}
    
    def obtener_saldos_todos_bancos(self) -> Dict:
        """
        Obtiene saldos de todos los bancos configurados.
        """
        resultado = {
            "propietario": self.propietario,
            "rfc": self.rfc,
            "fecha_consulta": datetime.now().isoformat(),
            "bancos": []
        }
        
        # Obtener saldo BBVA
        saldo_bbva = self.bbva.obtener_saldo_cuenta_principal()
        resultado["bancos"].append(saldo_bbva)
        
        # Obtener saldo Santander
        saldo_santander = self.santander.obtener_saldo_cuenta()
        resultado["bancos"].append(saldo_santander)
        
        # Calcular totales
        resultado["resumen"] = self._calcular_resumen(resultado["bancos"])
        
        return resultado
    
    def _calcular_resumen(self, bancos: List[Dict]) -> Dict:
        """
        Calcula un resumen consolidado de todos los bancos.
        """
        total_disponible = 0
        total_bloqueado = 0
        bancos_exitosos = 0
        
        for banco_data in bancos:
            if banco_data.get("estado") == "exitoso":
                total_disponible += banco_data.get("saldo_disponible", 0)
                total_bloqueado += banco_data.get("saldo_bloqueado", 0)
                bancos_exitosos += 1
        
        return {
            "saldo_total_disponible": total_disponible,
            "saldo_total_bloqueado": total_bloqueado,
            "saldo_total_neto": total_disponible - total_bloqueado,
            "bancos_activos": bancos_exitosos,
            "moneda": "MXN"
        }
    
    def obtener_movimientos_consolidados(self) -> Dict:
        """
        Obtiene movimientos de todos los bancos.
        """
        resultado = {
            "propietario": self.propietario,
            "rfc": self.rfc,
            "fecha_consulta": datetime.now().isoformat(),
            "movimientos_por_banco": {}
        }
        
        # Movimientos BBVA
        mov_bbva = self.bbva.obtener_movimientos_recientes(30)
        resultado["movimientos_por_banco"]["BBVA"] = mov_bbva
        
        # Movimientos Santander
        mov_santander = self.santander.obtener_movimientos(
            "2026-08-30",
            "2026-09-29"
        )
        resultado["movimientos_por_banco"]["Santander"] = mov_santander
        
        return resultado
    
    def generar_reporte_completo(self) -> Dict:
        """
        Genera un reporte completo de finanzas multibanco.
        """
        reporte = {
            "propietario": self.propietario,
            "rfc": self.rfc,
            "fecha_reporte": datetime.now().isoformat(),
            "seccion_saldos": self.obtener_saldos_todos_bancos(),
            "seccion_movimientos": self.obtener_movimientos_consolidados()
        }
        
        return reporte


if __name__ == "__main__":
    print("=" * 70)
    print("GESTOR MULTIBANCO - DASHBOARD FINANCIERO")
    print("=" * 70)
    print()
    
    gestor = GestorMultibanco()
    print(f"Propietario: {gestor.propietario}")
    print(f"RFC: {gestor.rfc}")
    print(f"Bancos: BBVA México + Santander México")
    print()
    
    # Obtener saldos de todos los bancos
    print("OBTENIENDO SALDOS EN TIEMPO REAL...")
    print("-" * 70)
    saldos = gestor.obtener_saldos_todos_bancos()
    print(saldos)
    print()
    
    # Obtener movimientos consolidados
    print("OBTENIENDO MOVIMIENTOS CONSOLIDADOS...")
    print("-" * 70)
    movimientos = gestor.obtener_movimientos_consolidados()
    print(movimientos)
    print()
    
    # Generar reporte completo
    print("REPORTE FINANCIERO COMPLETO")
    print("-" * 70)
    reporte = gestor.generar_reporte_completo()
    print(reporte)
