import pickle
import cv2
import numpy as np


def calcular_flujo(pickle_file):
    with open(pickle_file, 'rb') as f:
        data = pickle.load(f)

    total_count = data['total_count']
    video_duration_sec = data['video_duration_sec']

    if video_duration_sec > 0:
        flujo_vehicular_por_segundo = total_count / video_duration_sec
        flujo_vehicular_por_minuto = flujo_vehicular_por_segundo * 60
    else:
        flujo_vehicular_por_segundo = 0
        flujo_vehicular_por_minuto = 0

    # Crear una ventana con los resultados
    window_width = 520
    window_height = 280
    resultado = np.zeros((window_height, window_width, 3), dtype=np.uint8)
    resultado.fill(0)  # Fondo negro

    font = cv2.FONT_HERSHEY_TRIPLEX
    font_scale = 0.65
    color = (255, 255, 255)
    thickness = 0
    line_height = 30
    y0, dy = 50, 40

    lines = [
        "****RESULTADOS****",
        f"-TOTAL DE VEHICULOS: {total_count}",
        f"-DURACION DE LA MUESTRA: {video_duration_sec:.2f} seg",
        "",
        f"-Flujo vehicular= {flujo_vehicular_por_segundo:.2f} veh/seg",
        f"-Flujo vehicular= {flujo_vehicular_por_minuto:.2f} veh/min"
    ]

    for i, line in enumerate(lines):
        y = y0 + i * dy
        cv2.putText(resultado, line, (50, y), font, font_scale, color, thickness)

    cv2.imshow("Resultado del Flujo Vehicular", resultado)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
