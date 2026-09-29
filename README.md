# Algoritmos de Juan Davila Camarillo

## 📱 Proyecto: Sistema de Monitoreo de Actividad Bancaria

Sistema inteligente para detectar transacciones anómalas y prevenir bloqueos innecesarios en cuentas bancarias.

### 🎯 Características

- **Detección de Anomalías**: Identifica patrones sospechosos en transacciones
- **Análisis de Velocidad**: Detecta múltiples transacciones en poco tiempo
- **Control de Límites**: Monitorea límites diarios de monto y cantidad
- **Análisis Geográfico**: Identifica ubicaciones inusuales
- **Detección de Fraude**: Reconoce patrones de actividad fraudulenta
- **Generación de Reportes**: Estadísticas detalladas de actividad

### 🚀 Cómo Usar

```python
from monitoreo_actividad_bancaria import MonitoreoActividadBancaria

# Crear monitor
monitor = MonitoreoActividadBancaria(
    limite_transacciones_por_dia=10,
    limite_monto_diario=5000.0
)

# Registrar una transacción
resultado = monitor.registrar_transaccion(
    monto=500.0,
    tipo="compra",
    ubicacion="Centro Comercial - Ciudad A"
)

# Ver análisis
print(f"Riesgo de bloqueo: {resultado['riesgo_bloqueo']}")
print(f"Anomalías: {resultado['anomalias_detectadas']}")
print(f"Recomendación: {resultado['recomendacion']}")
```

### 📊 Niveles de Riesgo

- **BAJO**: Sin anomalías detectadas
- **MEDIO**: 1-2 anomalías
- **ALTO**: 3-4 anomalías
- **CRÍTICO**: 5+ anomalías

### 🔍 Tipos de Anomalías Detectadas

1. Exceso de transacciones en el día
2. Límite de monto diario excedido
3. Velocidad de transacciones sospechosa
4. Monto inusualmente alto
5. Ubicación geográfica inusual
6. Patrón de fraude detectado

### 📝 Autor

**Juan Davila Camarillo**

### 📄 Licencia

MIT License - Libre para usar y modificar
