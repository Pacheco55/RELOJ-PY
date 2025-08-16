
# Reloj Digital/Análogo - PIXELBITS Edition

![Python](https://img.shields.io/badge/Python-3.7+-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![Pygame](https://img.shields.io/badge/Audio-Pygame-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Version](https://img.shields.io/badge/Version-1.0-red)

**Aplicación de reloj multifuncional con interfaz gráfica profesional y sistema de alarmas inteligente**

*Una elegante aplicación de escritorio desarrollada por PIXELBITS Studios que combina la funcionalidad de un reloj digital y análogo tradicional con características modernas de alarmas personalizables y notificaciones sonoras.*

---

## **¿Por qué elegir nuestro Reloj Digital/Análogo?**

En la era digital actual, tener **control total sobre el tiempo** es esencial para la productividad. Esta aplicación no es solo un reloj, es un **centro de gestión temporal** que combina la elegancia visual del reloj análogo clásico con la precisión del display digital moderno.

### **Características Distintivas**

**Doble Modalidad de Visualización**
Alternancia instantánea entre modo digital con números grandes y claros, y modo análogo con manecillas tradicionales y números horarios. Interfaz limpia y profesional optimizada para cualquier entorno de trabajo.

**Sistema de Alarmas Avanzado**
Configuración personalizable de alarmas por hora y minuto, activación/desactivación con un clic, validación automática de horarios y notificaciones tanto visuales como sonoras.

**Experiencia Audio-Visual**
Sonidos personalizables para alarmas programadas, marcas sonoras cada hora para gestión de tiempo, soporte para archivos MP3 y sistema de notificaciones emergentes integrado.

**Interfaz de Usuario Intuitiva**
Diseño minimalista con controles claramente identificados, ventana redimensionable de 400x600 píxeles, botones de radio para selección de modo y campos de entrada validados para configuración de alarmas.

---

## **Capturas de Pantalla**

### **Interfaz Principal - Modo Digital**

<!-- Agregar imagen aquí -->
![Reloj Digital](<img width="545" height="627" alt="Image" src="https://github.com/user-attachments/assets/59e2304a-1713-4b9c-a939-9987d260d1cf" />)

*Vista del reloj en modo digital mostrando la hora actual con números grandes y legibles*

### **Interfaz Principal - Modo Análogo**

<!-- Agregar imagen aquí -->
![Reloj Análogo](<img width="543" height="626" alt="Image" src="https://github.com/user-attachments/assets/3de6005e-f71f-4630-87d6-bfb759d7dead" />)

*Vista del reloj en modo análogo con manecillas tradicionales y números horarios*

### **Panel de Configuración de Alarmas**

<!-- Agregar imagen aquí -->
![Configuración de Alarmas](<img width="567" height="198" alt="Image" src="https://github.com/user-attachments/assets/5f273d0c-0616-4280-9473-ee3671c8a164" />)

*Panel de control para configurar y gestionar alarmas personalizadas*

### **Notificación de Alarma Activa**

<!-- Agregar imagen aquí -->
![Alarma Activada](<img width="177" height="145" alt="Image" src="https://github.com/user-attachments/assets/9ff71603-c4df-4cac-8b42-d4f1777596f1" />)

*Ventana de notificación emergente cuando se activa una alarma programada*

---

## **Especificaciones Técnicas**

### **Requisitos del Sistema**

**Sistema Operativo**
Windows 10/11, macOS 10.14+, Linux Ubuntu 18.04+ o cualquier distribución con soporte Python 3.7+

**Python y Dependencias**
Python 3.7 o superior (recomendado Python 3.9+), Tkinter (incluido con Python estándar) y Pygame para funcionalidad de audio

**Recursos del Sistema**
RAM: 50MB mínimo, 100MB recomendado, CPU: Cualquier procesador moderno, almacenamiento: 5MB para la aplicación + archivos de sonido

**Archivos de Audio Opcionales**
alarm.mp3 para sonido de alarma personalizado, hour.mp3 para marca horaria y formato MP3 compatible con Pygame mixer

### **Instalación de Dependencias**

#### **Instalación Automática con pip**

```bash
pip install pygame
```

#### **Instalación Manual por Sistema Operativo**

**Windows**
```cmd
python -m pip install pygame
```

**macOS**
```bash
python3 -m pip install pygame
```

**Linux (Ubuntu/Debian)**
```bash
sudo apt-get install python3-pygame
# o alternativamente
pip3 install pygame
```

#### **Verificación de Instalación**

```python
import pygame
import tkinter as tk
print("Todas las dependencias instaladas correctamente")
```

---

## **Instalación y Configuración**

### **Descarga e Instalación**

**Paso 1: Clonar o descargar el repositorio**
```bash
git clone https://github.com/usuario/reloj-digital-analogo.git
cd reloj-digital-analogo
```

**Paso 2: Verificar dependencias**
```bash
python --version  # Debe ser 3.7+
pip install pygame
```

**Paso 3: Configurar archivos de sonido (opcional)**
Coloca los archivos `alarm.mp3` y `hour.mp3` en el mismo directorio que el script principal para habilitar las notificaciones sonoras personalizadas.

**Paso 4: Ejecutar la aplicación**
```bash
python reloj_digital_analogo.py
```

### **Archivos de Sonido Recomendados**

**alarm.mp3**
Sonido de alarma (recomendado: 3-5 segundos, tono distintivo), formato MP3 estándar, volumen moderado para evitar sobresaltos

**hour.mp3**
Marca horaria (recomendado: 1-2 segundos, tono suave), formato MP3 estándar, volumen bajo para no interrumpir el trabajo

---

## **Manual de Usuario**

### **Interfaz Principal**

**Selector de Modo**
Utiliza los botones de radio "Digital" y "Análogo" en la parte superior para alternar entre las visualizaciones. El cambio es instantáneo y mantiene la hora actual.

**Área de Visualización**
Canvas central de 300x300 píxeles que muestra el reloj según el modo seleccionado. En modo digital muestra números grandes en formato HH:MM:SS. En modo análogo presenta manecillas tradicionales con numeración horaria.

### **Sistema de Alarmas**

**Configuración de Alarma**
En el panel "Configurar Alarma", ingresa la hora (00-23) y minutos (00-59) deseados. Presiona "Activar Alarma" para programar la notificación. El sistema validará automáticamente los valores ingresados.

**Gestión de Alarmas**
Usa "Desactivar Alarma" para cancelar cualquier alarma activa. Puedes reconfigurar la hora sin necesidad de desactivar primero. Solo se puede tener una alarma activa a la vez.

### **Funcionalidades Automáticas**

**Actualización en Tiempo Real**
El reloj se actualiza cada segundo automáticamente mostrando la hora actual del sistema. No requiere intervención del usuario.

**Marcas Horarias**
El sistema reproduce automáticamente un sonido cada hora en punto (minuto 00, segundo 00) si está disponible el archivo `hour.mp3`.

**Notificaciones de Alarma**
Cuando se alcanza la hora programada, el sistema muestra una ventana emergente y reproduce el sonido de alarma si está disponible el archivo `alarm.mp3`.

---

## **Características Técnicas Avanzadas**

### **Arquitectura del Software**

**Clase Principal Clock**
Hereda de `tk.Tk` proporcionando una ventana principal robusta con gestión completa de eventos y estados del reloj.

**Sistema de Canvas Dinámico**
Utiliza `tk.Canvas` para renderizado vectorial de alta calidad tanto para números digitales como para manecillas análogas con cálculos trigonométricos precisos.

**Gestión de Estados**
Variables `tk.StringVar` para modo de reloj, control de alarmas con validación de entrada y gestión de archivos multimedia con pygame.mixer.

### **Algoritmos de Renderizado**

**Reloj Análogo**
Cálculos trigonométricos para posicionamiento de manecillas usando `math.pi` y funciones `cos/sin`. Manecilla de segundos (roja, 120px), manecilla de minutos (negra, 100px, grosor 3) y manecilla de horas (negra, 80px, grosor 5).

**Reloj Digital**
Renderizado de texto vectorial con fuente Arial 36pt bold. Formato HH:MM:SS con ceros a la izquierda y centrado automático en el canvas.

### **Sistema de Audio**

**Inicialización Pygame**
`mixer.init()` al arranque de la aplicación con manejo de excepciones para sistemas sin audio. Soporte para archivos MP3 estándar con `mixer.music.load()` y `mixer.music.play()`.

**Gestión de Errores de Audio**
Try-catch para archivos de sonido faltantes con fallback a notificaciones visuales únicamente. Mensaje de consola para marcas horarias cuando no hay audio disponible.

---

## **Casos de Uso**

### **Entorno de Oficina**

**Gestión de Reuniones**
Programa alarmas para recordatorios de juntas importantes. Visualización clara del tiempo durante videollamadas. Marcas horarias discretas para gestión del tiempo.

**Productividad Personal**
Técnica Pomodoro con alarmas de 25 minutos. Recordatorios de descansos programados. Seguimiento visual del tiempo en tareas específicas.

### **Uso Doméstico**

**Rutinas Diarias**
Alarmas para medicamentos con horarios específicos. Recordatorios de tareas domésticas programadas. Reloj de mesa digital elegante para cualquier habitación.

**Estudio y Trabajo Remoto**
Control de sesiones de estudio con límites de tiempo. Recordatorios de descansos saludables. Ambiente de trabajo organizado con gestión temporal clara.

### **Aplicaciones Educativas**

**Enseñanza de Conceptos Temporales**
Visualización dual digital/análoga para aprendizaje. Comprensión de manecillas y numeración horaria. Práctica de lectura de hora en ambos formatos.

**Gestión de Clases**
Temporizadores para actividades específicas. Alarmas de cambio de período o materia. Herramienta visual para estudiantes durante exámenes.

---

## **Personalización y Extensiones**

### **Modificaciones de Interfaz**

**Cambio de Colores**
Modifica `bg='white'` en la línea del Canvas para cambiar el fondo. Ajusta `fill='red'` para cambiar el color de la manecilla de segundos. Personaliza colores de manecillas de minutos y horas.

**Tamaño de Ventana**
Cambia `geometry("400x600")` para ajustar dimensiones. Modifica el tamaño del Canvas proporcionalmente. Ajusta las posiciones de texto y elementos gráficos.
---

## **Resolución de Problemas**

### **Problemas de Instalación**

**Error: No module named 'pygame'**
Ejecuta `pip install pygame` en la terminal. Verifica que pip esté actualizado con `pip --version`. En sistemas Linux, usa `pip3` en lugar de `pip`.

**Error de permisos en instalación**
Usa `pip install --user pygame` para instalación local. En sistemas Unix, considera `sudo pip3 install pygame`. Verifica permisos de escritura en el directorio de Python.

**Tkinter no encontrado**
En Ubuntu/Debian: `sudo apt-get install python3-tk`. En CentOS/RHEL: `sudo yum install tkinter`. Verifica instalación con `python -m tkinter`.

### **Problemas de Funcionamiento**

**Reloj no se actualiza**
Verifica que no hay bloqueos en el hilo principal. Reinicia la aplicación completamente. Comprueba el uso de CPU, debe ser mínimo.

**Sonidos no funcionan**
Verifica que los archivos `alarm.mp3` y `hour.mp3` existen. Confirma que pygame está correctamente instalado. Prueba reproducir archivos MP3 con otro reproductor.

**Alarma no activa**
Confirma que el formato de hora es correcto (HH:MM). Verifica que la alarma está marcada como activa. Comprueba que el reloj del sistema es correcto.

### **Problemas de Rendimiento**

**Uso alto de CPU**
El uso normal debe ser <1% de CPU en sistemas modernos. Cierra otras aplicaciones que consuman recursos. Considera aumentar el intervalo de actualización si es necesario.

**Interfaz lenta o congelada**
Verifica memoria RAM disponible (requiere <100MB). Cierra aplicaciones innecesarias. Reinicia la aplicación si persiste el problema.

---

## **Especificaciones de Rendimiento**

### **Métricas del Sistema**

**Consumo de Recursos**
RAM: 45-60MB durante operación normal, CPU: <1% en sistemas modernos, almacenamiento: 2MB para código + archivos de sonido

**Tiempos de Respuesta**
Inicio de aplicación: <2 segundos, cambio de modo digital/análogo: <0.5 segundos, activación de alarma: <0.1 segundos

**Precisión Temporal**
Actualización cada 1000ms (1 segundo), sincronización con reloj del sistema, precisión de alarmas: ±1 segundo

### **Compatibilidad**

**Versiones de Python Probadas**
Python 3.7, 3.8, 3.9, 3.10, 3.11 (recomendado)

**Sistemas Operativos Compatibles**
Windows 10/11, macOS Big Sur+, Ubuntu 18.04+, Debian 10+, CentOS 8+, Fedora 30+
---

## **Créditos y Desarrollo**

### **Desarrollo Principal**

**PIXELBITS Studios**
*Especialistas en aplicaciones de escritorio multiplataforma*
*Innovación en interfaces de usuario intuitivas*
*Desarrollo de software utilitario profesional*

### **Desarrollador Principal**

**Pacheco Julio**
*Arquitecto de software y especialista en Python/Tkinter*
*Diseñador de experiencias de usuario*
*Visionario en aplicaciones de productividad personal*

### **Tecnologías Utilizadas**

**Python 3.7+**: Lenguaje principal de desarrollo
**Tkinter**: Framework de interfaz gráfica nativa
**Pygame**: Motor de audio y multimedia
**DateTime**: Gestión de tiempo y fechas del sistema

---

## **Licencia**

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## **Soporte**

**Documentación**: Consulta este README para información completa

**Issues**: Reporta problemas en el repositorio de GitHub

**Email**: info@pixelbits.studio

**Actualizaciones**: Sigue el repositorio para recibir notificaciones de nuevas versiones

---

<div align="center">

### **Desarrollado con precisión por PIXELBITS Studios**

*Donde el tiempo encuentra la tecnología*

**[Website](https://pixelbits.studio) | [Email](mailto:info@pixelbits.studio) | [GitHub](https://github.com/pixelbits-studios)**

---

*Reloj Digital/Análogo - Gestión temporal inteligente para la era digital*

</div>
