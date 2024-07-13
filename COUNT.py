import cv2
import torch
from tracker import Tracker
import pickle
from calculate_flow import calcular_flujo  # Modificar importación

# Cargar el modelo YOLOv5 con pesos preentrenados
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)

# Cargar el video
cap = cv2.VideoCapture('ANALISIS_1.mp4')

count = 0
tracker = Tracker()

# Definir la línea para conteo (coordenadas ajustadas a la ROI)
line_start = (45, 108)
line_end = (260, 108)

# Definir la ROI
roi_x = 350
roi_y = 346
roi_width = 300
roi_height = 190

crossed_ids = set()

# Obtener el tiempo inicial en milisegundos
start_time_msec = cap.get(cv2.CAP_PROP_POS_MSEC)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 5 != 0:
        continue
    frame = cv2.resize(frame, (1020, 600))

    # Recortar la ROI del frame
    roi = frame[roi_y:roi_y + roi_height, roi_x:roi_x + roi_width]

    results = model(roi)
    list = []
    for index, rows in results.pandas().xyxy[0].iterrows():
        x = int(rows[0])
        y = int(rows[1])
        x1 = int(rows[2])
        y1 = int(rows[3])
        list.append([x, y, x1, y1])

    idx_bbox = tracker.update(list)
    for bbox in idx_bbox:
        x2, y2, x3, y3, id = bbox

        cv2.rectangle(roi, (x2, y2), (x3, y3), (0, 255, 0), 2)
        #cv2.putText(roi, str(id), (x2, y2), cv2.FONT_HERSHEY_PLAIN, 1, (0, 128, 0), 2)

        # Calcular el punto medio inferior del bounding box
        cx = (x2 + x3) // 2
        cy = y3

        cv2.circle(roi, (cx, cy), 3, (0, 0, 255), -2)

        # Verificar si el vehículo cruza la línea
        if line_start[1] - 10 < cy < line_start[1] + 10 and line_start[0] < cx < line_end[0]:
            crossed_ids.add(id)

    # Dibujar la línea en la ROI
    cv2.line(roi, line_start, line_end, (255, 0, 0), 2)

    # Crear un frame para mostrar el contador
    counter_frame = frame.copy()
    count_text = f"Nro. VEHICULOS: {len(crossed_ids)}"
    cv2.putText(counter_frame, count_text, (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 250, 250), 2)

    # Mostrar las dos ventanas
    cv2.imshow("ROI", roi)
    cv2.imshow("Contador", counter_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

# Obtener la duración del video en milisegundos al momento de finalizar
end_time_msec = cap.get(cv2.CAP_PROP_POS_MSEC)
# Convertir la duración a segundos
video_duration_sec = (end_time_msec - start_time_msec) / 1000.0

cap.release()
cv2.destroyAllWindows()

# Guardar los resultados
result_data = {
    'total_count': len(crossed_ids),
    'video_duration_sec': video_duration_sec  # Duración real del video en segundos
}

with open('result_data.pkl', 'wb') as f:
    pickle.dump(result_data, f)

# Llamar a la función para calcular y mostrar el flujo vehicular
calcular_flujo('result_data.pkl')
