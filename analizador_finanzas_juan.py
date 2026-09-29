"""
Analizador de Ingresos y Gastos
Para: Juan Davila Camarillo
Autor: Juan Davila Camarillo

Herramienta para analizar patrones de gasto e ingreso.
"""

from typing import List, Dict
from statistics import mean, stdev


class AnalizadorFinanzasJuan:
    """Analiza patrones financieros de Juan Davila Camarillo."""
    
    def __init__(self, propietario: str = "Juan Davila Camarillo"):
        self.propietario = propietario
        self.historial = []
    
    def registrar_movimiento(self, tipo: str, monto: float, categoria: str):
        """Registra un movimiento financiero."""
        self.historial.append({
            "tipo": tipo,  # ingreso o gasto
            "monto": monto,
            "categoria": categoria
        })
    
    def analizar_gastos(self) -> Dict:
        """Analiza los patrones de gasto."""
        gastos = [m["monto"] for m in self.historial if m["tipo"] == "gasto"]
        
        if not gastos:
            return {"propietario": self.propietario, "mensaje": "Sin gastos registrados"}
        
        return {
            "propietario": self.propietario,
            "total_gastos": sum(gastos),
            "promedio_gasto": mean(gastos),
            "gasto_maximo": max(gastos),
            "gasto_minimo": min(gastos),
            "desviacion_estandar": stdev(gastos) if len(gastos) > 1 else 0
        }
    
    def categorizar_gastos(self) -> Dict:
        """Agrupa gastos por categoría."""
        categorias = {}
        for m in self.historial:
            if m["tipo"] == "gasto":
                cat = m["categoria"]
                if cat not in categorias:
                    categorias[cat] = 0
                categorias[cat] += m["monto"]
        
        return {
            "propietario": self.propietario,
            "gastos_por_categoria": categorias,
            "categoria_mayor_gasto": max(categorias, key=categorias.get) if categorias else None
        }
    
    def ratio_ahorro(self) -> Dict:
        """Calcula el ratio de ahorro."""
        ingresos = sum(m["monto"] for m in self.historial if m["tipo"] == "ingreso")
        gastos = sum(m["monto"] for m in self.historial if m["tipo"] == "gasto")
        
        if ingresos == 0:
            ratio = 0
        else:
            ratio = ((ingresos - gastos) / ingresos) * 100
        
        return {
            "propietario": self.propietario,
            "ingresos_totales": ingresos,
            "gastos_totales": gastos,
            "ratio_ahorro_porcentaje": round(ratio, 2),
            "interpretacion": "Buen ahorro" if ratio > 20 else "Revisar gastos" if ratio < 0 else "Ahorro moderado"
        }


if __name__ == "__main__":
    analizador = AnalizadorFinanzasJuan()
    
    # Registrar movimientos
    analizador.registrar_movimiento("ingreso", 15000, "Salario")
    analizador.registrar_movimiento("ingreso", 3000, "Freelance")
    analizador.registrar_movimiento("gasto", 5000, "Vivienda")
    analizador.registrar_movimiento("gasto", 1200, "Alimentación")
    analizador.registrar_movimiento("gasto", 800, "Transporte")
    analizador.registrar_movimiento("gasto", 500, "Entretenimiento")
    
    print("ANÁLISIS DE FINANZAS - JUAN DAVILA CAMARILLO")
    print("=" * 50)
    print()
    print("Análisis de gastos:")
    print(analizador.analizar_gastos())
    print()
    print("Gastos por categoría:")
    print(analizador.categorizar_gastos())
    print()
    print("Ratio de ahorro:")
    print(analizador.ratio_ahorro())
