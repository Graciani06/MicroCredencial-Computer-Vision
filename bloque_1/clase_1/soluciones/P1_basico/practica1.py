import cv2
import numpy as np

# TODO: Crear y mostrar imagenes
image_gray = np.full((100, 200), 120, dtype=np.uint8)          # 1 canal, valor 120
image_blue = np.full((100, 200, 3), (255, 0, 0), dtype=np.uint8)  # 3 canales, BGR
cv2.imshow("image_gray", image_gray)
cv2.imshow("image_blue", image_blue)
print("Shape:", image_blue.shape)                              # (filas, columnas, canales)
print("Rows:", image_blue.shape[0])
print("Columns:", image_blue.shape[1])
print("Channels:", image_blue.shape[2])
print("Dtype:", image_blue.dtype)

cv2.waitKey(0)
cv2.destroyAllWindows()

# TODO: Leer de fichero
knights = cv2.imread("../data/knights.png")
if knights is None:
    print("Error: no se ha podido leer la imagen")
    exit()

cv2.imshow("knights", knights)
cv2.destroyAllWindows()

# TODO: Convertir a grayscale
knights_gray = cv2.cvtColor(knights, cv2.COLOR_BGR2GRAY)
cv2.imshow("knights_gray", knights_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# TODO: Convertir a blanco y negro
value, knights_bw = cv2.threshold(knights_gray, 100, 255, cv2.THRESH_BINARY)  # devuelve (umbral, imagen)
print("Channels:", knights_bw.shape)
print("Dtype:", knights_bw.dtype)
cv2.imshow("knights_bw", knights_bw)
cv2.waitKey(0)
cv2.destroyAllWindows()

# TODO: Negativo
knights_negative = 255 - knights
cv2.imshow("knights_negative", knights_negative)
cv2.waitKey(0)
cv2.destroyAllWindows()

# TODO: Multiplicar por escalar
knights_darker = cv2.multiply(knights, 0.5)
cv2.imshow("knights_darker", knights_darker)
cv2.waitKey(0)
cv2.destroyAllWindows()

# TODO: Sumar y combinar
chess = cv2.imread("../data/chessboard.png")                    # recuperamos la original
if chess is None:
    print("Error: no se ha podido leer la imagen")
    exit()
fusion = cv2.addWeighted(knights, 0.5, chess, 0.5, 0)   # 0.5*a + 0.5*b + 0
cv2.imshow("fusion", fusion)
cv2.waitKey(0)
cv2.destroyAllWindows()

# TODO: Lectura/escritura de pixeles
color1 = knights[20, 20]                                       # [fila, columna] -> [B G R]
print(color1)

knights[20, 20] = (0, 0, 255)

for r in range(20, 60):
    for c in range(30, 90):
        knights[r, c] = (0, 0, 255)                            # bloque rojo (lento: bucle en Python)
# knights[20:60, 30:90] = (0, 0, 255)                          # lo mismo, en una linea

cv2.imshow("write pixels", knights)
cv2.waitKey(0)
cv2.destroyAllWindows()

# TODO: Copia y clonado
knights_ref = knights                                         
knights_ref[:] = (0, 255, 0)
cv2.imshow("knights_ref", knights_ref)
cv2.imshow("knights", knights)
cv2.waitKey(0)

knights = cv2.imread("../data/knights.png")                    # recuperamos la original
if knights is None:
    print("Error: no se ha podido leer la imagen")
    exit()
knights_copy = knights.copy()                                  # copia real
knights_copy[:] = (0, 255, 0)
cv2.imshow("knights clone", knights_copy)
cv2.imshow("knights", knights)
cv2.waitKey(0)
cv2.destroyAllWindows()

# TODO: Crop
x, y, w, h = 450, 420, 70, 70
face = knights[y:y + h, x:x + w].copy()                        # [filas, columnas]
cv2.imshow("knights", knights)
cv2.imshow("face", face)
cv2.waitKey(0)
cv2.destroyAllWindows()

# TODO: Resize
face_big_linear = cv2.resize(face, (420, 420)) # por defecto INTER_LINEAR
cv2.imshow("face_big_linear", face_big_linear)

face_big_nearest = cv2.resize(face, (420, 420), interpolation=cv2.INTER_NEAREST)
cv2.imshow("face_big_nearest", face_big_nearest)
cv2.waitKey(0)
cv2.destroyAllWindows()

# TODO: Canales
b, g, r = cv2.split(knights)                                   # o knights[:, :, 0], [:, :, 1], [:, :, 2]
cv2.imshow("blue", b)
cv2.imshow("green", g)
cv2.imshow("red", r)
cv2.waitKey(0)
cv2.destroyAllWindows()

# TODO: HSV
hsv = cv2.cvtColor(knights, cv2.COLOR_BGR2HSV)                 # H [0,180), S [0,255], V [0,255]
h, s, v = cv2.split(hsv)
s = cv2.multiply(s,2.0)                          # saturacion x2 (satura en 255)
knights_sat = cv2.cvtColor(cv2.merge([h, s, v]), cv2.COLOR_HSV2BGR)
cv2.imshow("knights", knights)
cv2.imshow("saturation x2", knights_sat)
cv2.waitKey(0)
cv2.destroyAllWindows()


