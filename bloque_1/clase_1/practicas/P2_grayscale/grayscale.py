import cv2
import numpy as np


def meanBGR(img):
    """Gris como la media plana de los tres canales: (B + G + R) / 3.
    No usar cvtColor.
    Devuelve una imagen de 1 canal y tipo uint8.
    """
    # TODO: codificar la conversion
    return np.zeros(img.shape[:2], dtype=np.uint8)


def bt601BGR(img):
    """Gris segun la norma BT.601:  gray = 0.299*R + 0.587*G + 0.114*B.
    No usar cvtColor.
    Devuelve una imagen de 1 canal y tipo uint8.
    """
    # TODO: codificar la conversion
    return np.zeros(img.shape[:2], dtype=np.uint8)


def diff(img_a, img_b):
    """Diferencia absoluta entre dos imágenes."""
    # TODO: calcular la diferencia absoluta entre las dos imágenes
    return np.zeros_like(img_a)


# TODO: cargar la imagen
img = np.zeros((400, 400, 3), dtype=np.uint8)   # Borrar esta linea

# Convertir la imagen a escala de grises usando las funciones definidas
gray_1 = meanBGR(img)
gray_2 = bt601BGR(img)

# Calcular la diferencia entre las dos imágenes en escala de grises
# Multiplicar la diferencia por 5 para hacerla más visible
gray_diff = cv2.multiply(diff(gray_1, gray_2),5)

# TODO: Salvar las imágenes en escala de grises y la diferencia

# TODO: mostrar las imágenes en escala de grises y la diferencia


cv2.destroyAllWindows()
