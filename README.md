# Algoritmos Personalizados para Juan Davila Camarillo

## 📊 Suite Completa de Gestión Financiera Personal

Este repositorio contiene algoritmos reales personalizados para **Juan Davila Camarillo** diseñados para gestionar y analizar finanzas personales.

### 📁 Contenido

#### Algoritmos de Seguridad Bancaria (Educativos)
1. `deteccion_fraude.py` - Detección de señales de fraude
2. `encriptacion_segura.py` - Cifrado de datos con Fernet
3. `autenticacion_segura.py` - Autenticación con hash PBKDF2
4. `monitoreo_actividad_bancaria.py` - Monitoreo de anomalías
5. `validacion_transferencias.py` - Validación de datos

#### Algoritmos de Gestión Financiera Personal (REALES)
1. **`gestor_finanzas_juan.py`** - Gestión completa de ingresos y gastos
2. **`analizador_finanzas_juan.py`** - Análisis de patrones de gasto
3. **`planificador_presupuesto_juan.py`** - Planificación de presupuesto mensual

### 🚀 Características de los Algoritmos Personalizados

#### Gestor de Finanzas
- Registro de ingresos y gastos
- Cálculo de balance neto
- Generación de resúmenes financieros
- Clasificación de ingresos y gastos

#### Analizador de Finanzas
- Análisis estadístico de gastos (promedio, máximo, mínimo)
- Agrupación por categoría
- Cálculo de ratio de ahorro
- Interpretación de resultados

#### Planificador de Presupuesto
- Establecimiento de presupuestos por categoría
- Seguimiento de gastos realizados
- Alertas cuando se alcanza el 90% del presupuesto
- Alertas de excedencia
- Reporte de estado mensual

### 💻 Cómo Usar

```python
# Ejemplo: Gestor de Finanzas
from gestor_finanzas_juan import GestorFinanzasJuan

gestor = GestorFinanzasJuan()
gestor.agregar_ingreso("Salario", 15000)
gestor.agregar_gasto("Vivienda", "Renta", 5000)
print(gestor.calcular_balance())
```

```python
# Ejemplo: Planificador de Presupuesto
from planificador_presupuesto_juan import PlanificadorPresupuestoJuan

planificador = PlanificadorPresupuestoJuan(presupuesto_mensual=18000)
planificador.establecer_presupuesto_categoria("Vivienda", 5000)
planificador.registrar_gasto_categoria("Vivienda", 5000)
print(planificador.obtener_estado_presupuesto())
```

### 📈 Ejemplo de Salida

```
GESTOR FINANCIERO PERSONAL - Juan Davila Camarillo
Total Ingresos: $18,000.00
Total Gastos: $8,500.00
Balance Neto: $9,500.00
Estado: Positivo ✓
```

### ⚠️ Notas Importantes

- Los algoritmos de seguridad son **educativos** y no reemplazan sistemas bancarios certificados
- Los algoritmos de gestión financiera son **personalizados y reales** para Juan Davila Camarillo
- No introduzas datos sensibles reales en el repositorio público
- Estos son ejemplos para aprendizaje y gestión personal

### 📝 Autor

**Juan Davila Camarillo**

### 📅 Fecha de Creación

2026-09-29

### 📄 Licencia

MIT License
