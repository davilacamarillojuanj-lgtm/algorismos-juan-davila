"""
Sistema de Saldos en Tiempo Real - BBVA México
Propietario: Juan Davila Camarillo
RFC: DACJ871001KTA
Autor: Juan Davila Camarillo

Conexión segura a API BBVA para obtener saldos en tiempo real.
Requiere credenciales en archivo .env
"""

import os
import requests
from typing import Dict, List
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


class SistemaBalanceBBVA:
    """Sistema de conexión a BBVA México para obtener saldos."""
    
    def __init__(self):
        self.propietario = "Juan Davila Camarillo"
        self.rfc = "DACJ871001KTA"
        self.banco = "BBVA México"
        self.base_url = os.getenv("BBVA_API_URL", "https://api.bbva.mx")
        self.api_key = os.getenv("BBVA_API_KEY")
        self.user_id = os.getenv("BBVA_USER_ID")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        self.saldos_cache = {}
        self.ultima_actualizacion = None
    
    def obtener_saldo_cuenta_principal(self) -> Dict:
        """
        Obtiene el saldo de la cuenta principal de BBVA.
        Requiere configuración en .env con BBVA_API_KEY y BBVA_USER_ID
        """
        try:
            if not self.api_key or not self.user_id:
                return {
                    "estado": "error",
                    "mensaje": "Credenciales no configuradas. Verifica archivo .env",
                    "banco": self.banco
                }
            
            # Endpoint para obtener cuentas del usuario
            url = f"{self.base_url}/accounts/{self.user_id}/balances"
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                self.saldos_cache["bbva"] = data
                self.ultima_actualizacion = datetime.now().isoformat()
                
                return {
                    "estado": "exitoso",
                    "banco": self.banco,
                    "propietario": self.propietario,
                    "rfc": self.rfc,
                    "saldo_disponible": data.get("availableBalance", 0),
                    "saldo_total": data.get("totalBalance", 0),
                    "moneda": data.get("currency", "MXN"),
                    "fecha_actualizacion": self.ultima_actualizacion
                }
            else:
                return {
                    "estado": "error",
                    "mensaje": f"Error en API BBVA: {response.status_code}",
                    "banco": self.banco,
                    "detalles": response.text
                }
        
        except requests.exceptions.RequestException as e:
            return {
                "estado": "error",
                "mensaje": f"Error de conexión a BBVA: {str(e)}",
                "banco": self.banco
            }
    
    def obtener_todas_cuentas(self) -> Dict:
        """
        Obtiene todas las cuentas asociadas en BBVA.
        """
        try:
            if not self.api_key or not self.user_id:
                return {
                    "estado": "error",
                    "mensaje": "Credenciales no configuradas",
                    "banco": self.banco
                }
            
            url = f"{self.base_url}/accounts"
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code == 200:
                cuentas = response.json()
                return {
                    "estado": "exitoso",
                    "banco": self.banco,
                    "propietario": self.propietario,
                    "rfc": self.rfc,
                    "cantidad_cuentas": len(cuentas),
                    "cuentas": cuentas,
                    "fecha_actualizacion": datetime.now().isoformat()
                }
            else:
                return {
                    "estado": "error",
                    "mensaje": f"Error: {response.status_code}",
                    "banco": self.banco
                }
        
        except requests.exceptions.RequestException as e:
            return {
                "estado": "error",
                "mensaje": f"Error de conexión: {str(e)}",
                "banco": self.banco
            }
    
    def obtener_movimientos_recientes(self, dias: int = 30) -> Dict:
        """
        Obtiene los movimientos recientes de la cuenta.
        """
        try:
            if not self.api_key or not self.user_id:
                return {
                    "estado": "error",
                    "mensaje": "Credenciales no configuradas",
                    "banco": self.banco
                }
            
            url = f"{self.base_url}/accounts/{self.user_id}/transactions"
            params = {"days": dias}
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            
            if response.status_code == 200:
                transacciones = response.json()
                return {
                    "estado": "exitoso",
                    "banco": self.banco,
                    "propietario": self.propietario,
                    "rfc": self.rfc,
                    "periodo_dias": dias,
                    "cantidad_transacciones": len(transacciones),
                    "transacciones": transacciones,
                    "fecha_consulta": datetime.now().isoformat()
                }
            else:
                return {
                    "estado": "error",
                    "mensaje": f"Error: {response.status_code}",
                    "banco": self.banco
                }
        
        except requests.exceptions.RequestException as e:
            return {
                "estado": "error",
                "mensaje": f"Error de conexión: {str(e)}",
                "banco": self.banco
            }


if __name__ == "__main__":
    print("=" * 70)
    print("SISTEMA DE SALDOS EN TIEMPO REAL - BBVA MÓXICO")
    print("=" * 70)
    print()
    
    bbva = SistemaBalanceBBVA()
    print(f"Propietario: {bbva.propietario}")
    print(f"RFC: {bbva.rfc}")
    print(f"Banco: {bbva.banco}")
    print()
    
    # Obtener saldo principal
    print("Obteniendo saldo principal...")
    saldo = bbva.obtener_saldo_cuenta_principal()
    print(saldo)
    print()
    
    # Obtener todas las cuentas
    print("Obteniendo todas las cuentas...")
    cuentas = bbva.obtener_todas_cuentas()
    print(cuentas)
    print()
    
    # Obtener movimientos recientes
    print("Obteniendo movimientos de los últimos 30 días...")
    movimientos = bbva.obtener_movimientos_recientes(30)
    print(movimientos)
