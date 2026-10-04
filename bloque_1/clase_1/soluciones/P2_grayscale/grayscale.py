import cv2
import numpy as np


def meanBGR(img):
    """Gris como la media plana de los tres canales: (B + G + R) / 3.
    No usar cvtColor.
    Devuelve una imagen de 1 canal y tipo uint8.
    """
    b, g, r = cv2.split(img)
    return (0.333 * r + 0.333 * g + 0.333 * b).astype(np.uint8)


def bt601BGR(img):
    """Gris segun la norma BT.601:  gray = 0.299*R + 0.587*G + 0.114*B.
    No usar cvtColor.
    Devuelve una imagen de 1 canal y tipo uint8.
    """
    b, g, r = cv2.split(img)
    return (0.299 * r + 0.587 * g + 0.114 * b).astype(np.uint8)


def diff(img_a, img_b):
    """Diferencia absoluta entre dos imágenes."""
    return cv2.absdiff(img_a, img_b)


img = cv2.imread("../data/knights.png", cv2.IMREAD_COLOR)
if img is None:
    print("Error: no se pudo leer la imagen.")
    exit(1)

# Convertir la imagen a escala de grises usando las funciones definidas
gray_1 = meanBGR(img)
gray_2 = bt601BGR(img)

# Calcular la diferencia entre las dos imágenes en escala de grises
# Multiplicar la diferencia por 5 para hacerla más visible
gray_diff = cv2.multiply(diff(gray_1, gray_2), 5)

# Salvar las imágenes en escala de grises y la diferencia
cv2.imwrite("gray_mean.png", gray_1)
cv2.imwrite("gray_bt601.png", gray_2)
cv2.imwrite("gray_diff.png", gray_diff)
# mostrar las imágenes en escala de grises y la diferencia
cv2.imshow("gray mean", gray_1)
cv2.imshow("gray bt601", gray_2)
cv2.imshow("gray diff", gray_diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
