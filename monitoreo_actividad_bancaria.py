"""
Algoritmo de Monitoreo de Actividad Bancaria
Detecta transacciones anómalas para prevenir bloqueos de cuenta
Autor: Juan Davila Camarillo
"""

from datetime import datetime, timedelta
from typing import List, Dict, Tuple
import statistics

class MonitoreoActividadBancaria:
    """
    Sistema de monitoreo para detectar actividades anómalas en cuentas bancarias.
    Previene bloqueos innecesarios mediante análisis inteligente de transacciones.
    """
    
    def __init__(self, limite_transacciones_por_dia: int = 10,
                 limite_monto_diario: float = 5000.0,
                 ventana_tiempo_minutos: int = 60):
        """
        Inicializa el sistema de monitoreo.
        
        Args:
            limite_transacciones_por_dia: Máximo de transacciones permitidas por día
            limite_monto_diario: Monto máximo a transferir en un día
            ventana_tiempo_minutos: Ventana de tiempo para análisis de velocidad
        """
        self.limite_transacciones = limite_transacciones_por_dia
        self.limite_monto_diario = limite_monto_diario
        self.ventana_tiempo = ventana_tiempo_minutos
        self.historial_transacciones = []
        self.patrones_normales = {}
        
    def registrar_transaccion(self, monto: float, tipo: str, 
                             ubicacion: str, timestamp: datetime = None) -> Dict:
        """
        Registra una transacción en el sistema de monitoreo.
        
        Args:
            monto: Cantidad de dinero de la transacción
            tipo: Tipo de transacción (transferencia, compra, retiro, etc.)
            ubicacion: Ubicación geográfica de la transacción
            timestamp: Fecha y hora de la transacción
            
        Returns:
            Diccionario con análisis de la transacción
        """
        if timestamp is None:
            timestamp = datetime.now()
            
        transaccion = {
            'monto': monto,
            'tipo': tipo,
            'ubicacion': ubicacion,
            'timestamp': timestamp
        }
        
        # Análisis de anomalías
        anomalias = self._detectar_anomalias(transaccion)
        
        # Registrar en historial
        self.historial_transacciones.append(transaccion)
        
        return {
            'transaccion': transaccion,
            'anomalias_detectadas': anomalias,
            'riesgo_bloqueo': self._calcular_riesgo_bloqueo(anomalias),
            'recomendacion': self._generar_recomendacion(anomalias)
        }
    
    def _detectar_anomalias(self, transaccion: Dict) -> List[str]:
        """
        Detecta anomalías en una transacción.
        
        Returns:
            Lista de anomalías detectadas
        """
        anomalias = []
        hoy = transaccion['timestamp'].date()
        
        # 1. Verificar límite de transacciones por día
        transacciones_hoy = [t for t in self.historial_transacciones 
                            if t['timestamp'].date() == hoy]
        if len(transacciones_hoy) >= self.limite_transacciones:
            anomalias.append("Exceso de transacciones en el día")
        
        # 2. Verificar monto total diario
        monto_diario = sum(t['monto'] for t in transacciones_hoy)
        if monto_diario + transaccion['monto'] > self.limite_monto_diario:
            anomalias.append("Límite de monto diario excedido")
        
        # 3. Detectar transacciones muy rápidas (velocidad anómala)
        if self._velocidad_anomala(transaccion['timestamp']):
            anomalias.append("Velocidad de transacciones sospechosa")
        
        # 4. Detectar monto inusualmente alto
        if self._monto_inusual(transaccion['monto']):
            anomalias.append("Monto inusualmente alto")
        
        # 5. Detectar ubicación geográfica sospechosa
        if self._ubicacion_sospechosa(transaccion['ubicacion']):
            anomalias.append("Ubicación geográfica inusual")
        
        # 6. Detectar patrones de fraude conocidos
        if self._patron_fraude(transaccion):
            anomalias.append("Patrón de fraude detectado")
        
        return anomalias
    
    def _velocidad_anomala(self, timestamp: datetime) -> bool:
        """Verifica si hay demasiadas transacciones en poco tiempo."""
        ventana_inicio = timestamp - timedelta(minutes=self.ventana_tiempo)
        transacciones_ventana = [t for t in self.historial_transacciones
                                if ventana_inicio <= t['timestamp'] <= timestamp]
        return len(transacciones_ventana) > 5
    
    def _monto_inusual(self, monto: float) -> bool:
        """Verifica si el monto es inusualmente alto."""
        if not self.historial_transacciones:
            return False
        
        montos = [t['monto'] for t in self.historial_transacciones]
        promedio = statistics.mean(montos)
        desviacion = statistics.stdev(montos) if len(montos) > 1 else 0
        
        # Anomalía si es 3 desviaciones estándar mayor al promedio
        return monto > (promedio + 3 * desviacion)
    
    def _ubicacion_sospechosa(self, ubicacion: str) -> bool:
        """Verifica si la ubicación es inusual comparada con el historial."""
        if not self.historial_transacciones:
            return False
        
        ubicaciones_previas = set(t['ubicacion'] for t in self.historial_transacciones[-30:])
        return ubicacion not in ubicaciones_previas and len(ubicaciones_previas) > 0
    
    def _patron_fraude(self, transaccion: Dict) -> bool:
        """Detecta patrones conocidos de fraude."""
        # Patrón: múltiples transacciones a diferentes ubicaciones en poco tiempo
        hace_una_hora = transaccion['timestamp'] - timedelta(hours=1)
        transacciones_recientes = [t for t in self.historial_transacciones
                                   if t['timestamp'] > hace_una_hora]
        
        ubicaciones_diferentes = len(set(t['ubicacion'] for t in transacciones_recientes))
        
        return ubicaciones_diferentes > 3
    
    def _calcular_riesgo_bloqueo(self, anomalias: List[str]) -> str:
        """
        Calcula el nivel de riesgo de bloqueo de cuenta.
        
        Returns:
            'BAJO', 'MEDIO', 'ALTO' o 'CRITICO'
        """
        cantidad_anomalias = len(anomalias)
        
        if cantidad_anomalias == 0:
            return "BAJO"
        elif cantidad_anomalias <= 2:
            return "MEDIO"
        elif cantidad_anomalias <= 4:
            return "ALTO"
        else:
            return "CRITICO"
    
    def _generar_recomendacion(self, anomalias: List[str]) -> str:
        """Genera una recomendación basada en las anomalías detectadas."""
        if not anomalias:
            return "Transacción segura. Procedimiento normal."
        
        if "Patrón de fraude detectado" in anomalias:
            return "⚠️ CONTACTA A TU BANCO INMEDIATAMENTE. Actividad sospechosa detectada."
        
        if "Ubicación geográfica inusual" in anomalias:
            return "Verifica que esta ubicación sea correcta."
        
        if any("límite" in a.lower() for a in anomalias):
            return "Has alcanzado límites de transacciones. Espera hasta mañana."
        
        return "Transacción registrada con precaución. Monitorea tu cuenta."
    
    def generar_reporte(self) -> Dict:
        """Genera un reporte detallado de la actividad bancaria."""
        if not self.historial_transacciones:
            return {"mensaje": "No hay transacciones registradas"}
        
        montos = [t['monto'] for t in self.historial_transacciones]
        
        return {
            'total_transacciones': len(self.historial_transacciones),
            'monto_total': sum(montos),
            'monto_promedio': statistics.mean(montos),
            'monto_maximo': max(montos),
            'monto_minimo': min(montos),
            'desviacion_estandar': statistics.stdev(montos) if len(montos) > 1 else 0,
            'ultima_transaccion': self.historial_transacciones[-1]['timestamp'],
            'alertas_activas': self._contar_alertas()
        }
    
    def _contar_alertas(self) -> int:
        """Cuenta el número de alertas activas en las últimas 24 horas."""
        hace_24h = datetime.now() - timedelta(hours=24)
        alertas = 0
        
        for transaccion in self.historial_transacciones:
            if transaccion['timestamp'] > hace_24h:
                anomalias = self._detectar_anomalias(transaccion)
                alertas += len(anomalias)
        
        return alertas


# Ejemplo de uso
if __name__ == "__main__":
    # Crear monitor
    monitor = MonitoreoActividadBancaria(
        limite_transacciones_por_dia=10,
        limite_monto_diario=5000.0
    )
    
    # Simular transacciones
    print("=== SISTEMA DE MONITOREO DE ACTIVIDAD BANCARIA ===")
    print()
    
    # Transacción normal
    resultado1 = monitor.registrar_transaccion(
        monto=500.0,
        tipo="compra",
        ubicacion="Centro Comercial - Ciudad A"
    )
    print(f"Transacción 1 - Riesgo: {resultado1['riesgo_bloqueo']}")
    print(f"Recomendación: {resultado1['recomendacion']}")
    print()
    
    # Transacción con monto alto
    resultado2 = monitor.registrar_transaccion(
        monto=4000.0,
        tipo="transferencia",
        ubicacion="Centro Comercial - Ciudad A"
    )
    print(f"Transacción 2 - Riesgo: {resultado2['riesgo_bloqueo']}")
    print(f"Anomalías: {resultado2['anomalias_detectadas']}")
    print(f"Recomendación: {resultado2['recomendacion']}")
    print()
    
    # Transacción en ubicación inusual
    resultado3 = monitor.registrar_transaccion(
        monto=300.0,
        tipo="retiro",
        ubicacion="País Diferente - Ciudad B"
    )
    print(f"Transacción 3 - Riesgo: {resultado3['riesgo_bloqueo']}")
    print(f"Anomalías: {resultado3['anomalias_detectadas']}")
    print(f"Recomendación: {resultado3['recomendacion']}")
    print()
    
    # Reporte final
    print("=== REPORTE DE ACTIVIDAD ===")
    reporte = monitor.generar_reporte()
    for clave, valor in reporte.items():
        print(f"{clave}: {valor}")