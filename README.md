# 💱 Conversor de Divisas Pro & Analizador de Tendencias

> **Sistema híbrido de automatización financiera que combina la captura de datos en tiempo real mediante APIs con análisis estadístico descriptivo y visualización de datos.**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Pandas](https://img.shields.io/badge/Pandas-Análisis-green) ![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualización-orange)

## 📖 Descripción del Proyecto

Este proyecto es una solución integral para la conversión de divisas que va más allá de un simple cálculo matemático. El sistema integra tres componentes críticos:
1.  **Consumo de Datos en Tiempo Real:** Interacción con la API de *ExchangeRate* para obtener tasas oficiales de mercado.
2.  **Persistencia y Registro:** Almacenamiento local de cada operación en formato CSV para trazabilidad histórica.
3.  **Business Intelligence (BI):** Módulo de análisis que procesa el historial para generar *insights* visuales sobre el comportamiento del usuario.

## 🚀 Características Principales

* **🌐 Integración con API REST:** Uso de la librería `requests` para obtener datos financieros actualizados globalmente.
* **💾 Módulo de Persistencia:** Implementación de manejo de archivos (CSV) con lógica de inicialización y escritura segura de datos.
* **📉 Análisis Estadístico:** Procesamiento de grandes volúmenes de datos históricos mediante la librería **Pandas**.
* **📊 Visualización de Datos:** Generación de gráficos de barras con **Matplotlib** para identificar tendencias de uso y volúmenes de conversión por moneda.
* **🛡️ Robusta Gestión de Errores:** Control de excepciones para fallas de red, tiempos de espera (*timeouts*) y entradas de usuario no numéricas.

## 🛠️ Tecnologías Utilizadas

* **Python:** Lenguaje base.
* **Pandas:** Limpieza y transformación de datos históricos.
* **Matplotlib:** Generación de reportes gráficos.
* **Requests:** Comunicación con servicios web externos.
* **CSV/Datetime:** Manejo de formatos de fecha y almacenamiento local.

## 📂 Estructura del Proyecto

```bash
📁 Conversor-Divisas/
│
├── 📁 src/
│   ├── conversor.py      # Lógica de conversión, consumo de API y persistencia.
│   └── analisis.py       # Módulo de procesamiento de datos y graficación.
│
├── historial_conversiones.csv  # Base de datos histórica (generada automáticamente).
└── README.md             # Documentación.
```

## 📊 Diccionario de Datos (Historial)

El sistema genera un archivo `historial_conversiones.csv` con la siguiente estructura, permitiendo auditorías de datos y análisis posterior:

| Campo | Descripción |
| :--- | :--- |
| **fecha** | Estampa de tiempo de la operación (YYYY-MM-DD HH:MM:SS). |
| **moneda_base** | Moneda de referencia del sistema (predeterminado USD). |
| **monto_origen** | Cantidad ingresada por el usuario para convertir. |
| **moneda_origen** | Divisa de entrada seleccionada. |
| **moneda_destino** | Divisa de salida para el cálculo. |
| **resultado** | Valor calculado según la tasa de cambio real obtenida de la API. |

## 🔧 Instalación y Uso

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/josuegiraldos/conversor-divisas.git](https://github.com/josuegiraldos/conversor-divisas.git)
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install requests pandas matplotlib
    ```

3.  **Ejecutar el Conversor:**
    ```bash
    python src/conversor.py
    ```

4.  **Generar Análisis Gráfico:**
    ```bash
    python src/analisis.py
    ```

## 🧠 Lógica de Análisis

El archivo `analisis.py` realiza un proceso **ETL** simplificado para transformar los registros en información visual:
* **Extracción:** Carga el historial desde el archivo CSV generado por el conversor.
* **Transformación:** Utiliza **Pandas** para convertir tipos de datos, limpiar entradas y agrupar la información por moneda de origen.
* **Carga (Visual):** Emplea **Matplotlib** para renderizar un gráfico de barras que identifica los volúmenes de conversión por divisa.

---

## 👤 Autor

**Josué Gabriel Giraldo Suárez**

---
*Este proyecto forma parte de un portafolio profesional enfocado en ingeniería de datos, integración de APIs y automatización de procesos.*