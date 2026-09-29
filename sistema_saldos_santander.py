"""
Sistema de Saldos en Tiempo Real - Santander México
Propietario: Juan Davila Camarillo
RFC: DACJ871001KTA
Autor: Juan Davila Camarillo

Conexión segura a API Santander para obtener saldos en tiempo real.
Requiere credenciales en archivo .env
"""

import os
import requests
from typing import Dict, List
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


class SistemaBalanceSantander:
    """Sistema de conexión a Santander México para obtener saldos."""
    
    def __init__(self):
        self.propietario = "Juan Davila Camarillo"
        self.rfc = "DACJ871001KTA"
        self.banco = "Santander México"
        self.base_url = os.getenv("SANTANDER_API_URL", "https://api.santander.com.mx")
        self.api_key = os.getenv("SANTANDER_API_KEY")
        self.account_id = os.getenv("SANTANDER_ACCOUNT_ID")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        self.saldos_cache = {}
        self.ultima_actualizacion = None
    
    def obtener_saldo_cuenta(self) -> Dict:
        """
        Obtiene el saldo de la cuenta en Santander.
        Requiere configuración en .env con SANTANDER_API_KEY y SANTANDER_ACCOUNT_ID
        """
        try:
            if not self.api_key or not self.account_id:
                return {
                    "estado": "error",
                    "mensaje": "Credenciales no configuradas. Verifica archivo .env",
                    "banco": self.banco
                }
            
            # Endpoint para obtener saldo de cuenta
            url = f"{self.base_url}/accounts/{self.account_id}/balance"
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                self.saldos_cache["santander"] = data
                self.ultima_actualizacion = datetime.now().isoformat()
                
                return {
                    "estado": "exitoso",
                    "banco": self.banco,
                    "propietario": self.propietario,
                    "rfc": self.rfc,
                    "saldo_disponible": data.get("availableBalance", 0),
                    "saldo_total": data.get("totalBalance", 0),
                    "saldo_bloqueado": data.get("blockedBalance", 0),
                    "moneda": data.get("currency", "MXN"),
                    "fecha_actualizacion": self.ultima_actualizacion
                }
            else:
                return {
                    "estado": "error",
                    "mensaje": f"Error en API Santander: {response.status_code}",
                    "banco": self.banco,
                    "detalles": response.text
                }
        
        except requests.exceptions.RequestException as e:
            return {
                "estado": "error",
                "mensaje": f"Error de conexión a Santander: {str(e)}",
                "banco": self.banco
            }
    
    def obtener_productos(self) -> Dict:
        """
        Obtiene todos los productos (cuentas, tarjetas, etc) en Santander.
        """
        try:
            if not self.api_key:
                return {
                    "estado": "error",
                    "mensaje": "Credenciales no configuradas",
                    "banco": self.banco
                }
            
            url = f"{self.base_url}/products"
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code == 200:
                productos = response.json()
                return {
                    "estado": "exitoso",
                    "banco": self.banco,
                    "propietario": self.propietario,
                    "rfc": self.rfc,
                    "cantidad_productos": len(productos),
                    "productos": productos,
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
    
    def obtener_movimientos(self, desde_fecha: str, hasta_fecha: str) -> Dict:
        """
        Obtiene movimientos en un rango de fechas.
        Formato de fecha: YYYY-MM-DD
        """
        try:
            if not self.api_key or not self.account_id:
                return {
                    "estado": "error",
                    "mensaje": "Credenciales no configuradas",
                    "banco": self.banco
                }
            
            url = f"{self.base_url}/accounts/{self.account_id}/transactions"
            params = {
                "from_date": desde_fecha,
                "to_date": hasta_fecha
            }
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            
            if response.status_code == 200:
                transacciones = response.json()
                return {
                    "estado": "exitoso",
                    "banco": self.banco,
                    "propietario": self.propietario,
                    "rfc": self.rfc,
                    "desde_fecha": desde_fecha,
                    "hasta_fecha": hasta_fecha,
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
    print("SISTEMA DE SALDOS EN TIEMPO REAL - SANTANDER MÓXICO")
    print("=" * 70)
    print()
    
    santander = SistemaBalanceSantander()
    print(f"Propietario: {santander.propietario}")
    print(f"RFC: {santander.rfc}")
    print(f"Banco: {santander.banco}")
    print()
    
    # Obtener saldo
    print("Obteniendo saldo de cuenta...")
    saldo = santander.obtener_saldo_cuenta()
    print(saldo)
    print()
    
    # Obtener productos
    print("Obteniendo productos...")
    productos = santander.obtener_productos()
    print(productos)
    print()
    
    # Obtener movimientos
    print("Obteniendo movimientos...")
    movimientos = santander.obtener_movimientos("2026-09-01", "2026-09-29")
    print(movimientos)
