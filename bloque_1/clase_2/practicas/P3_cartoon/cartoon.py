import cv2
import numpy as np

IMAGE = "../data/dog.jpg"


def cartoonize(img):
    """Convierte img en una imagen con estilo propio...

    Args:
        img: imagen de entrada, en color (BGR).

    Returns:
        La imagen con el efecto, en BGR (uint8) y del mismo tamaño que img.
    """
    ## TODO: CODE HERE
    result = img.copy()
    ## END TODO
    return result


def photo_effects(img):
    """Los efectos que ya trae OpenCV en el módulo photo, para compararlos con el propio.

    Args:
        img: imagen de entrada, en color (BGR).

    Returns:
        Diccionario {nombre de ventana: imagen} con cada efecto.
    """
    sketch_gray, sketch_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.02)   # dos resultados
    return {
        "stylization": cv2.stylization(img, sigma_s=60, sigma_r=0.45),
        "edgePreservingFilter": cv2.edgePreservingFilter(img, flags=cv2.RECURS_FILTER, sigma_s=60, sigma_r=0.4),
        "pencilSketch (gray)": sketch_gray,
        "pencilSketch (colour)": sketch_color,
        "detailEnhance": cv2.detailEnhance(img, sigma_s=10, sigma_r=0.15),
    }


## Cargar la imagen en color
img = cv2.imread(IMAGE)
if img is None:
    print("Error: could not read the image")
    exit(1)

cartoon = cartoonize(img)
cv2.imshow("cartoon", cartoon)
for name, effect in photo_effects(img).items():
    cv2.imshow(name, effect)
cv2.waitKey(0)
cv2.destroyAllWindows()
