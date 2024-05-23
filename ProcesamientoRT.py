# Importamos las librerias
import cv2
import numpy as np
 
# esta programacion va a tener 4 modos de ejecución ( lo utilizo con los nuemros del teclado 0.1.2 y 3 segun el codig ASSCI)

# Modos de ejecucion
#vc = 0 --> 48  # """Captura de video"""
#fd = 1 --> 49  # """Filtro desenfoque"""
#fe = 2 --> 50  # """Filtro detector de esquinas"""
#fb = 3 --> 51  # """Filtro de Bordes"""

# Lo primer que realizo es crear un diccionario con las caracteristicas de las esquinas que quiero determinar
# Parametros para detector de esquinas
esquinas_param = dict(maxCorners = 500,    # Es el n° Maximo de esquinas a detectar " si fuera un documento solo utilizo 4 esquinas"
                      qualityLevel = 0.2,  # Determino el Umbral minimo para que me detecte las esquinas
                      minDistance = 15,    # Distacia entre pixeles de una ezquina a otra esquina
                      blockSize = 9)       # Area de pixeles que evaluo para detectar las esquinas (9) pixeles

# Modo
mood = 48 # inicializo un modo con la tecla (0)la cual tiene un codigo ASSCI de 48, entonces el programa
# ejecuta en la primera intervencion con la """captura de video"""

# Creo la Video Captura
cap = cv2.VideoCapture(0)

# Creamos un ciclo para ejecutar nuestros Frames
while True:
    # Leemos los fotogramas
    ret, frame = cap.read()

    # Decidimos el mood, aqui inicio con los IF & elif


    # Normal => inicio con este modo si quiero una captura de video Normal
    if mood == 48: 
        # Mostramos los frames
        resultado = frame

    # Desenfoque (tecla 1)
    elif mood == 49: # 
        # Modificamos frames
        resultado = cv2.blur(frame, (10, 10)) # si oprimo la tecla (1), voy a remplazar la varaible resultado 
        #con un filtro de desenfoque de camara con el siguiente comando (cv2.blur) y lo que le tengo que entregar al comando
        #es (frame = que es la imagen a la cual le quiero aplicar el filtro) y un kerne de desenfoque (13,13) => basicamente es
        # una mascara de pixeles que va a desenfocar la imagen, puedo aplificar o disminuir: entre mayor sean los nuemeros mas desenfoque va haber.
        # """este es muy utilizado para metodos de estraccion de carcateristicas"""

    # Bordes (tecla 3)
    elif mood == 51: #aqui estoy preguntando si quiero que se ejecute la deteccion de bordes
        # Modificamos frames
        resultado = cv2.Canny(frame, 135, 150)  # inicio utilizando el comando (cv2.Canny)el cual hace una detección de bordes; le entrego
        # (frame => es decir la imagen a la cual quiero realizarle la deteccion de bordes)
        # igualmente una UMBRAL min y max de deteccion de bordes (135, 150) 
        #esto quiere decir si el GRADIENTE de intencidad supera el UMBRAL SUPERIOR es considerado como un BORDE.
        # si el GRADIENTE de intencidad pasa por debajo del UMBRAL INFERIOR tambien seraconsiderado como un BORDE
        # Es importante experiemntar con diferentes valores, por que estos difieren dependiendo de la camara que este utilizando y par las condiciones ambientales y de luz.


    # Esquinas (tecla 2)
    elif mood == 50: # aqui estoy preguntando si quiero que se ejecute la detección de esquinas
        # Obtenemos los frames
        resultado = frame # en esta variable muestro los frames, por que voy a dibujar los Frames en RGB pero voy a procesar en escala de GRICES
        # Conversion a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # => aqui estoy convieriendo los frames a escala de grises (cv2.COLOR_BGR2GRAY)
        
        esquinas = cv2.goodFeaturesToTrack(gray, **esquinas_param)# utilizo este comando para calcular las caracteristicas de las esquinas
        # le estoy etregando la Imagen en escala de grises(gray)  
        # le entrego las caracteristicas que quiero encotrar acompañado de 2 asteriscos (**esquinas_param) esto ya lo defini en la linea 15.
        # todo esto lo almaceno en la variable esquinas, la cual va a contener caracteristicas con los parametro definidos en el inicio.

      
        
        
        
        
        if esquinas is not None: # primero pregunto si en esquinas hay algo, por que puede existir la posibilidad de que no capte nada en los parametros definidos en el inicio.
            # Pasamos a Iterar si encontramos parametros
            for x, y in np.float32(esquinas).reshape(-1,2): # (for x, y) inicia iterando a sacar las coordenas en  (x & y) que va encontrando de las (500) esquinas
                # (np.float32) con estecomando basicamente le estoy asignando un formato a los valores que estoy extrayendo
                # Convertimos en enteros
                x,y = int(x), int(y) # => con este comando estoy combirtiendo los valores a  enteros, por que no hay pixeles decimales
                # Dibujamos la ubicacion de las esquinas
                cv2.circle(resultado, (x,y), 10, (255,0,0), 1) # => aqui estoy dibuijando un circulo en cada uno de sus valores

   
   
    # por ultimo Si presionamos otra tecla
    elif mood != 48 or mood != 49 or mood != 50 or mood != 51 or mood != -1:
        # No hacemos nada
        resultado = frame

        # Imprimimos mensaje
        print('TECLA INCORRECTA')


    # Mostramos los Frames
    cv2.imshow("VIDEO CAPTURA", resultado)

    # Cerramos con lectura de teclado
    t = cv2.waitKey(1)
    # Salimos
    if t == 27:
        break
    # Modificamos Mood
    elif t != -1:
        mood = t

# Liberamos la VideoCaptura
cap.release()
# Cerramos la ventana
cv2.destroyAllWindows()
