# Tecnicas-de-Procesamiento-en-Tiempo-real
Hola, chicos en este repositorio encontrarán la  explicación del codigo, de visión artificial, diapositivas, instaladores, y por supuesto el código programado en Python.

### Conceptos introductorios:
- En este repositorio se expondrá a una amplia gama de temas interesantes como manipulación de imágenes y videos, mejora de imágenes, filtrado, detección de bordes, detección y seguimiento de objetos, detección de rostros y el módulo de aprendizaje profundo con OpenCV.
- Para iniciar recomiendo ver algunos conceptos introductorios sobre los diferentes filtros de procesamiento que puedes utilizar en vision artificial.



### Instalación del entorno:
- Para iniciar con la programación debes de instalar Python y visualStudio Code

### Desenfoque, Bordes, y Esquinas:
- INICIAMOS con la programación;  en este primer script buscamos unir muchos conceptos como lo son:

  - Declaracion de librerias.
  - Captura de video en tiempo real.
  - Lectura del teclado.
  
- Despues de implementar estos conceptos, añadimos 3 tecnicas de procesamiento de imagenes como lo son:

  - Desenfoque de camara.
  - Deteccion de bordes.
  - Deteccion de esquinas.


# Desenfoque de Cámara. # (Se ejecuta al opimir la tecla # 1)
- este se utiliza mucho en los metodos de extracción de caracteristicas debido a que estos metodos tiene un (GRADIENTE NUMERICO) lo que se hace antes de aplicar el gradiente numerico, lo que se hace es suavisar un poco la imagen(es decir desenfocar un poco la imagen para que el Greadienate numerico tenga mejores resultados y por ende la extraccion de caracteristicas tenga mejores resultados.)

observese que si modifica el KERNEL del linea ... (13, 13) a (29, 29) el desenfoque va a ser mucho mayor. por lo general en las tecnicas de extraccion de caracteristicas no se usan desenfoques tan fueretes, sino suabizar un poquito la imagen nada mas.

(Definición: GRADIENTE NUMERICO-)=> En el contexto del video, el gradiente numérico se calcula para cada cuadro del video, proporcionando información sobre los cambios en la intensidad de los pixels a lo largo del tiempo. Esta información se puede utilizar para identificar y localizar objetos en movimiento, así como para predecir su trayectoria futura.

1. Reconocimiento de objetos: El gradiente numérico juega un papel importante en el reconocimiento de objetos, ya que proporciona información sobre la forma y los contornos de los objetos en las imágenes. Al analizar el gradiente en diferentes regiones de la imagen, se pueden extraer características distintivas que permiten identificar y clasificar objetos.

2. Seguimiento de movimiento: En aplicaciones de seguimiento de movimiento, el gradiente numérico se utiliza para identificar y rastrear objetos en movimiento en secuencias de video. Al calcular el gradiente en cada cuadro del video y analizar los cambios a lo largo del tiempo, se puede predecir la trayectoria de los objetos y seguir su movimiento.

3. Robótica y control de movimiento: En robótica y control de movimiento, el gradiente numérico se utiliza para guiar el movimiento de robots y vehículos autónomos. Al analizar el gradiente de imágenes del entorno, se pueden identificar obstáculos, determinar la trayectoria y evitar colisiones.


# Detección de Esquinas. (se ejecuta al oprimir la tecla # 2)
- va a detectar las 500 esquinas que le di por parametron en la linea 15.
TECNICAS DE OCR: En la visión por computador, las técnicas de OCR (Reconocimiento Óptico de Caracteres) que funcionan con la detección de esquinas son particularmente útiles para extraer texto de documentos escaneados o imágenes capturadas en entornos no controlados.


- VBEn la visión por computador, las técnicas de OCR (Reconocimiento Óptico de Caracteres) que funcionan con la detección de esquinas son particularmente útiles para extraer texto de documentos escaneados o imágenes capturadas en entornos no controlados.

las técnicas basadas en la detección de esquinas aprovechan las características geométricas de los documentos para mejorar la precisión y el rendimiento del reconocimiento.

Funcionamiento:

0. Detección de esquinas: El primer paso consiste en identificar las esquinas de las regiones que contienen texto, como páginas de libros, recibos o carteles. Esto se puede lograr utilizando algoritmos de detección de bordes, técnicas de segmentación de regiones o redes neuronales convolucionales.

1. Panorámica de imágenes: La detección de esquinas se utiliza para identificar puntos de referencia clave en imágenes consecutivas, lo que permite alinear y unir las imágenes para crear panorámicas o vistas de gran angular.

2. Reconstrucción 3D: Las esquinas de los objetos proporcionan pistas importantes sobre su forma y estructura tridimensional. La detección de esquinas se puede utilizar para reconstruir modelos 3D de objetos a partir de imágenes 2D.

3. Robótica y navegación: En robótica y navegación, la detección de esquinas se utiliza para identificar obstáculos, localizar puntos de referencia y guiar el movimiento de robots autónomos.

4. Realidad aumentada: La detección de esquinas se puede utilizar para superponer información digital sobre objetos del mundo real, alineando la información digital con las esquinas detectadas en la imagen de la cámara.

5. Reconocimiento de objetos: Las esquinas pueden ser características distintivas de objetos, y su detección se puede utilizar para identificar y clasificar objetos en imágenes.

6. Seguimiento de objetos: La detección de esquinas se puede utilizar para rastrear objetos en movimiento identificando y siguiendo sus esquinas a lo largo de una secuencia de imágenes.

7. Análisis de textura: Las esquinas pueden ser indicadores de patrones y texturas en las imágenes. La detección de esquinas se puede utilizar para analizar la textura de superficies y materiales.

8. Control de calidad: En el control de calidad industrial, la detección de esquinas se puede utilizar para identificar defectos o imperfecciones en productos manufacturados.

9. Asistencia a la conducción: En los sistemas de asistencia a la conducción, la detección de esquinas se puede utilizar para identificar señales de tráfico, carriles y otros elementos relevantes para la conducción segura.

10. Monitoreo de infraestructuras: La detección de esquinas se puede utilizar para inspeccionar infraestructuras como puentes, edificios y carreteras para detectar grietas, daños u otras anomalías.

# Detección de Bordes. (se ejecuta al oprimir la tecla # 3)
La detección de bordes es una técnica fundamental en la visión por computador que se utiliza para identificar los límites entre diferentes regiones de una imagen. Estos bordes pueden corresponder a cambios bruscos en la intensidad de los pixels, como los contornos de objetos, texturas o estructuras en la escena. La detección de bordes proporciona información valiosa para diversas tareas de análisis de imágenes y comprensión del entorno visual.



Gracias por su atencion

Mauricio Erazo Arango