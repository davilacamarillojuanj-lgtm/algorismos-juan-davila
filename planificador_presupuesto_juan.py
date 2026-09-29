"""
Planificador de Presupuesto Mensual
Para: Juan Davila Camarillo
Autor: Juan Davila Camarillo

Herramienta para planificar y controlar presupuesto mensual.
"""

from typing import Dict, List
from datetime import datetime


class PlanificadorPresupuestoJuan:
    """Planificador de presupuesto para Juan Davila Camarillo."""
    
    def __init__(self, presupuesto_mensual: float):
        self.propietario = "Juan Davila Camarillo"
        self.presupuesto_mensual = presupuesto_mensual
        self.presupuesto_por_categoria = {}
        self.gastos_realizados = {}
    
    def establecer_presupuesto_categoria(self, categoria: str, monto: float):
        """Establece presupuesto para una categoría."""
        self.presupuesto_por_categoria[categoria] = monto
        if categoria not in self.gastos_realizados:
            self.gastos_realizados[categoria] = 0
    
    def registrar_gasto_categoria(self, categoria: str, monto: float):
        """Registra un gasto en una categoría."""
        if categoria not in self.gastos_realizados:
            self.gastos_realizados[categoria] = 0
        self.gastos_realizados[categoria] += monto
    
    def obtener_estado_presupuesto(self) -> Dict:
        """Obtiene el estado actual del presupuesto."""
        estado = {
            "propietario": self.propietario,
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "presupuesto_mensual_total": self.presupuesto_mensual,
            "categorias": []
        }
        
        total_presupuestado = 0
        total_gastado = 0
        
        for categoria, presupuesto in self.presupuesto_por_categoria.items():
            gastado = self.gastos_realizados.get(categoria, 0)
            disponible = presupuesto - gastado
            porcentaje_utilizado = (gastado / presupuesto * 100) if presupuesto > 0 else 0
            
            estado["categorias"].append({
                "categoria": categoria,
                "presupuesto": presupuesto,
                "gastado": gastado,
                "disponible": disponible,
                "porcentaje_utilizado": round(porcentaje_utilizado, 2),
                "estado": "OK" if disponible >= 0 else "EXCEDIDO"
            })
            
            total_presupuestado += presupuesto
            total_gastado += gastado
        
        estado["resumen"] = {
            "total_presupuestado": total_presupuestado,
            "total_gastado": total_gastado,
            "total_disponible": total_presupuestado - total_gastado,
            "porcentaje_utilizado_general": round(total_gastado / total_presupuestado * 100, 2) if total_presupuestado > 0 else 0
        }
        
        return estado
    
    def alertas_presupuesto(self) -> List[str]:
        """Genera alertas si se exceden presupuestos."""
        alertas = []
        
        for categoria, presupuesto in self.presupuesto_por_categoria.items():
            gastado = self.gastos_realizados.get(categoria, 0)
            if gastado > presupuesto:
                exceso = gastado - presupuesto
                alertas.append(f"⚠️ {categoria}: Excedido ${exceso:.2f}")
            elif gastado >= presupuesto * 0.9:
                alertas.append(f"📊 {categoria}: Cercano al límite (90% utilizado)")
        
        if not alertas:
            alertas.append("✓ Presupuesto bajo control")
        
        return alertas


if __name__ == "__main__":
    planificador = PlanificadorPresupuestoJuan(presupuesto_mensual=18000)
    
    # Establecer presupuestos por categoría
    planificador.establecer_presupuesto_categoria("Vivienda", 5000)
    planificador.establecer_presupuesto_categoria("Alimentación", 2000)
    planificador.establecer_presupuesto_categoria("Transporte", 1000)
    planificador.establecer_presupuesto_categoria("Entretenimiento", 1000)
    planificador.establecer_presupuesto_categoria("Ahorros", 4000)
    
    # Registrar algunos gastos
    planificador.registrar_gasto_categoria("Vivienda", 5000)
    planificador.registrar_gasto_categoria("Alimentación", 1500)
    planificador.registrar_gasto_categoria("Transporte", 800)
    planificador.registrar_gasto_categoria("Entretenimiento", 400)
    planificador.registrar_gasto_categoria("Ahorros", 3000)
    
    print("PLANIFICADOR DE PRESUPUESTO - JUAN DAVILA CAMARILLO")
    print("=" * 60)
    print()
    
    estado = planificador.obtener_estado_presupuesto()
    print(f"Presupuesto Total Mensual: ${estado['presupuesto_mensual_total']}")
    print()
    print("Estado por Categoría:")
    for cat in estado["categorias"]:
        print(f"  {cat['categoria']}: ${cat['gastado']:.2f} / ${cat['presupuesto']:.2f} ({cat['porcentaje_utilizado']}%) [{cat['estado']}]")
    
    print()
    print("Resumen General:")
    resumen = estado["resumen"]
    print(f"  Total Presupuestado: ${resumen['total_presupuestado']:.2f}")
    print(f"  Total Gastado: ${resumen['total_gastado']:.2f}")
    print(f"  Total Disponible: ${resumen['total_disponible']:.2f}")
    
    print()
    print("Alertas:")
    for alerta in planificador.alertas_presupuesto():
        print(f"  {alerta}")
