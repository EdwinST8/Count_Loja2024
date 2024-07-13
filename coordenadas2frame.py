import cv2

# Cargar el video
cap = cv2.VideoCapture('ANALISIS_1.mp4')


# Obtener el tamaño del frame completo
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"Tamaño del frame completo: {frame_width} x {frame_height}")

# Función de callback para el mouse
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Coordenadas del clic: ({x}, {y})")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1280, 660))

    cv2.imshow("FRAME", frame)
    cv2.setMouseCallback("FRAME", click_event)  # Establecer la función de callback del mouse
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
