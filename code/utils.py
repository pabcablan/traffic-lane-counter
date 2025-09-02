def line_crossed(centroidX, centroidY, line):
    """
    Siendo cx1 el punto de inicio de la linea y 
    cx2 el punto final de la linea, y sabiendo que 
    para ser una linea horizontal cy1 == cy2, si
    el objeto tiene centroide x que se encuentre 
    entre la señalada y centroide y que pasen por 
    las indicadas con un margen de 10 pixeles
    es decir, si el objeto esta a menos de 10 pixeles
    lo cuenta.

    Entonces el objeto pasa por esa linea.
    """
    return line["cx1"] <= centroidX <= line["cx2"] and abs(centroidY - line["cy1"]) <= 10


def speed_calc(prev_obj, actual_obj, fps):
    """
    Calcula la velocidad de un objeto dado su posición previa y actual.
    
    Parámetros:
        prev_obj: tuple (x_prev, y_prev, frame_prev), posición previa.
        actual_obj: tuple (x_actual, y_actual, frame_actual), posición actual.
        fps: int, frames por segundo del video.
    
    Retorna:
        float, velocidad en píxeles por segundo.
    """
    x_prev, y_prev, prev_frame = prev_obj
    x_actual, y_actual, actual_frame = actual_obj

    distance = ((x_actual - x_prev) ** 2 + (y_actual - y_prev) ** 2) ** 0.5
    time = (actual_frame - prev_frame) / fps
    return distance / time if time > 0 else 0