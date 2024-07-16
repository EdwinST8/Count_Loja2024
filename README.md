# Count_Loja2024
Contador para calcular el flujo vehicular utilizando Yolov5.

Se debe clonar el repositorio de Yolov5 como primera instancia,
El script principal COUNT.py carga el video y los pesos, además de otras funciones
como la creación de una ROI en la zona analizada. Además se dibuja una línea contabiizadora
de los vehículos que transitan. Existe una función que halla el punto medio de los bounding boxes
que al entrar en contacto con la línea contabilizadora se aumenta una unidad en el frame de un cantador.
También se crea una lista de IDs para que las detecciones no se contabilicen más de una vez.

Por otro lado los scripts auxiliares tracker.py y calculate_flow.py, ayudan en el seguimiento de las detecciones que Yolov5 capta a través de los pesos entrenados con datos personalizados; y aplican la fórmula del flujo vehicular utlizando la cantidad de vehiculos detectados y el tiempo de video que trascurrió o el tiempo total del video al finalizar el frame.
El video ANALISIS_1.mp4 se lo encuentra en el siguiente link de YouTube: https://youtu.be/bVpb_LQ-5Lg
En el repositorio se adjuntan los pesos entrenados con una base de datos personalizada captada en la ciudad de Loja-Ecuador en el año 2024, esta base de datos se la encuentra en Roboflow (https://universe.roboflow.com/base-datos-l24/basedatos_l24/dataset/7).
