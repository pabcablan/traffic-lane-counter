import cv2
from utils import line_crossed, speed_calc

# Variables iniciales
video = 'tráfico01.mp4'
go = True
max_tracking = 14

lines_dic = [
    {"cx1": 480, "cy1": 850, "cx2": 580, "cy2": 850},
    {"cx1": 610, "cy1": 850, "cx2": 720, "cy2": 850},
    {"cx1": 990, "cy1": 750, "cx2": 1090, "cy2": 750},
    {"cx1": 1320, "cy1": 900, "cx2": 1470, "cy2": 900},
    {"cx1": 1180, "cy1": 640, "cx2": 1210, "cy2": 640},
    {"cx1": 1420, "cy1": 730, "cx2": 1500, "cy2": 730},
    {"cx1": 1630, "cy1": 770, "cx2": 1770, "cy2": 770}
]

# Ciclo principal
while go:
    cap = cv2.VideoCapture(video)
    counter = [0 for _ in lines_dic]
    object_ids = [0 for _ in lines_dic]

    track_obj = []
    for _ in lines_dic:
        track_obj.append({})

    if not cap.isOpened():
        print("Error: No se pudo abrir el archivo de video.")
        break

    bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=300, varThreshold=50, detectShadows=False)
    frames_counter = 0

    while True:
        r, frame = cap.read()
        if not r:
            cap.release()
            break

        frames_counter += 1
        mask = bg_subtractor.apply(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)))
        _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        fps = cap.get(cv2.CAP_PROP_FPS)

        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            centroidx = x + w // 2
            centroidy = y + h // 2

            if cv2.contourArea(contour) < 500 or w > 420:
                continue

            for i, line in enumerate(lines_dic):
                if line_crossed(centroidx, centroidy, line):
                    matching_object = next((objct_id for objct_id, (old_centroidx, old_centroidy, last_seen) in track_obj[i].items()
                    if abs(centroidx - old_centroidx) < 50 and abs(centroidy - old_centroidy) < 50), None)

                    if matching_object is not None:
                        obj_prev = track_obj[i][matching_object]
                        track_obj[i][matching_object] = (centroidx, centroidy, frames_counter)
                        speed = speed_calc(obj_prev, track_obj[i][matching_object], fps)
                        if speed > 0:
                            print(f"Velocidad de carril {i + 1}: {speed:.2f} píxeles/seg")
                    else:
                        track_obj[i][object_ids[i]] = (centroidx, centroidy, frames_counter)
                        counter[i] += 1
                        object_ids[i] += 1

        for i, _ in enumerate(lines_dic):
            expired_ids = [objct_id for objct_id, (_, _, last_seen) in track_obj[i].items() if frames_counter - last_seen > max_tracking]
            for objct_id in expired_ids:
                del track_obj[i][objct_id]

        for i, line in enumerate(lines_dic):
            text = f"Carril {i + 1}: {counter[i]}"
            cv2.line(frame, (line["cx1"], line["cy1"]), (line["cx2"], line["cy2"]), (0, 255, 255), 3)
            cv2.putText(frame, text, (line["cx1"], line["cy1"] - 15), cv2.FONT_HERSHEY_DUPLEX, 0.5, (250, 50, 255), 2)

        # Redimensionar el video procesado (En caso que los videos no se vean bien)
        # scale_percent = 70  # Cambia este valor para ajustar la escala
        # width = int(frame.shape[1] * scale_percent / 100)
        # height = int(frame.shape[0] * scale_percent / 100)
        # dim = (width, height)
        # resized_frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

        cv2.imshow("Máscara", mask)
        cv2.imshow("Detección de Vehículos", frame)

        if cv2.waitKey(27) & 0xFF == ord('s'):
            go = False
            break

    cap.release()
    cv2.destroyAllWindows()

# Imprimir el conteo final por carril
print("\n========== Conteo de Vehículos por Carril ==========")
for i, count in enumerate(counter):
    print(f"🚗 Carril {i + 1}: {count} vehículos detectados")
print("====================================================")
