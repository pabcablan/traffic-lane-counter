# 🚦 Contador de Vehículos por Carril  

![Python Version](https://img.shields.io/badge/Python-%3E%3D3.8-blue)  ![OpenCV](https://img.shields.io/badge/OpenCV-%3E%3D4.0-green)  ![Status](https://img.shields.io/badge/status-completed-success)  

## 📌 Descripción  

Este proyecto implementa un **sistema de conteo de vehículos en tráfico urbano** mediante visión por computador. Utilizando **Python** y **OpenCV**, el programa procesa un vídeo de entrada y:  

- Detecta vehículos en movimiento.  
- Rastrea su trayectoria para evitar duplicados.  
- Determina cruces en líneas de conteo predefinidas.  
- Genera estadísticas en tiempo real diferenciadas por carril.  

Es una herramienta orientada a la **monitorización de tráfico** en escenarios simulados.  


## ⚙️ Funcionamiento  

El flujo básico del sistema es:  

1. **Preprocesamiento del vídeo** → lectura frame a frame y redimensionamiento opcional.  
2. **Sustracción de fondo (`MOG2`)** → separación de objetos en movimiento del entorno estático.  
3. **Extracción de contornos** → filtrado según área y posición para descartar ruido.  
4. **Seguimiento de centroides** → evitar conteos repetidos.  
5. **Detección de cruces de línea** → validación de paso de vehículos en cada carril.  
6. **Visualización en vivo** → líneas, rectángulos, centroides y contadores superpuestos.  


## 📂 Estructura del Proyecto  

| Directorio | Archivos | Descripción |
|------------|----------|-------------|
| **/code**  | [`main.py`](/code/main.py) | Script principal que implementa la detección y conteo de vehículos usando OpenCV. Gestiona la sustracción de fondo, detección de contornos, seguimiento de objetos y visualización en tiempo real. |
|            | [`utils.py`](/code/utils.py) | Módulo de utilidades con funciones auxiliares como detección de cruces de línea y cálculo de velocidad. |
|            | [`tráfico.mp4`](/code/utils.py) | Video de muestra para pruebas del sistema. |
| **/docs**  | [`memoria.pdf`](/docs/memoria.pdf) | Explicación detallada del desarrollo, las decisiones de diseño y análisis de los resultados obtenidos. |

> **Notas útiles:**  
> - El escalado del vídeo puede ajustarse con `scale_percent` (líneas 85–89 del código).  
> - Si se aplica redimensionamiento, sustituir `frame` por `resized_frame` (línea 92).  
## 🛠️ Requisitos

Para ejecutar este proyecto necesitarás:

* **Python 3.8 o superior**
* **Biblioteca principal:**
  * OpenCV (≥ 4.0)

### Instalación de dependencias

```bash
# Instalar dependencia principal
pip install opencv-python
```

## 🚀 Instalación y Ejecución

### Paso 1: Clonar el repositorio

```bash
git clone https://github.com/pabcablan/traffic-lane-counter
cd traffic-lane-counter
```

### Paso 2: Preparar el vídeo de entrada

* El vídeo de muestra `tráfico.mp4` está incluido en la carpeta `/cide` del repositorio

```python
# Localización en MAIN.PY donde configurar la ruta del vídeo
video = 'tráfico01.mp4'  # Cambiar por tu archivo o ruta
```

### Paso 3: Ejecutar el programa

```bash
# Desde el directorio raíz del proyecto
python code/MAIN.PY
```

### Controles durante la ejecución

* Presiona `s` para detener la ejecución
* Las ventanas muestran el vídeo original con anotaciones y la máscara de detección


## 📷 Ejemplo de Salida

Durante la ejecución, el sistema muestra los siguientes elementos visuales en tiempo real:

![](https://github.com/user-attachments/assets/0abc1b41-8e5f-4ed5-9c43-0be849b38934)


**Elementos visuales:**
- 🚦 **Líneas carril**: Delimitan los puntos de conteo para cada carril
- 📊 **Contadores**: Muestran el número actual de vehículos detectados por carril 
- 🔍 **Máscara**: Aunque no se muestra en el GIF, el sistema también abre una ventana con la máscara de sustracción de fondo, útil para depuración y ajuste de parámetros

**Salida por consola:**
```
Velocidad de carril 1: 142.36 píxeles/seg
Velocidad de carril 3: 98.74 píxeles/seg
Velocidad de carril 2: 115.92 píxeles/seg
...

========== Conteo de Vehículos por Carril ==========
🚗 Carril 1: 24 vehículos detectados
🚗 Carril 2: 18 vehículos detectados
🚗 Carril 3: 31 vehículos detectados
...
====================================================
```


## 👥 Autores

- [Pablo Herrera González](https://github.com/D4rk-h) – Algoritmos y análisis computacional.
- [Pablo Cabeza Lantigua](https://github.com/pabcablan) – Procesamiento de vídeo y optimización.


## 📄 Licencia

Este proyecto está licenciado bajo la licencia GNU General Public License v3.0. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

**Nota**: Este proyecto fue desarrollado como trabajo académico para la asignatura **Fundamentos de los Sistemas Inteligentes** de la [Universidad de Las Palmas de Gran Canaria](https://www.ulpgc.es/).
