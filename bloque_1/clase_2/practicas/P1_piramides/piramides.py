import cv2

IMAGE = "../data/dog.jpg"


def downscale_pyr(img, steps):
    """Reduce img a la mitad steps veces seguidas.

    Args:
        img: imagen de entrada, en escala de grises.
        steps: número de veces que se reduce a la mitad.

    Returns:
        La imagen reducida: 2**steps veces más pequeña en ancho y en alto.
    """
    ## TODO: CODE HERE
    result = img.copy()
    ## END TODO
    return result


def upscale_pyr(img, steps):
    """Amplía img al doble steps veces seguidas.

    Args:
        img: imagen de entrada, en escala de grises.
        steps: número de veces que se amplía al doble.

    Returns:
        La imagen ampliada: 2**steps veces más grande en ancho y en alto.
    """
    ## TODO: CODE HERE
    result = img.copy()
    ## END TODO
    return result


def resize_nearest(img, size):
    """Redimensiona img al tamaño size.

    Args:
        img: imagen que se redimensiona.
        size: tamaño de salida como (ancho, alto).

    Returns:
        img redimensionada a size.
    """
    ## TODO: CODE HERE
    result = img.copy()
    ## END TODO
    return result


def fix_size(img, height, width):
    """Recorta img a height filas y width columnas, quedándose con la esquina superior izquierda.

    Args:
        img: imagen que se recorta; tiene que medir al menos height x width.
        height: número de filas de la salida.
        width: número de columnas de la salida.

    Returns:
        La esquina superior izquierda de img, de height filas y width columnas.
    """
    ## TODO: CODE HERE
    result = img.copy()
    ## END TODO
    return result


def difference(a, b, alpha):
    """Diferencia absoluta entre a y b, multiplicada por alpha para que se vea.

    Args:
        a, b: imágenes del mismo tamaño y tipo.
        alpha: factor por el que se multiplica la diferencia.

    Returns:
        La diferencia amplificada, en uint8.
    """
    return cv2.multiply(cv2.absdiff(a, b), alpha)


def show(windows):
    """Muestra cada imagen en su ventana y espera a que se pulse una tecla.

    Args:
        windows: diccionario {nombre de ventana: imagen}.
    """
    for name, image in windows.items():
        cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


## Cargar la imagen en escala de grises
img = cv2.imread(IMAGE, cv2.IMREAD_GRAYSCALE)
if img is None:
    print("Error: could not read the image")
    exit(1)
height, width = img.shape


## 1. Reducir: pyrDown down_steps veces frente a un único resize al mismo tamaño
down_steps = 3
small_pyr = downscale_pyr(img, down_steps)
small_height, small_width = small_pyr.shape
small_resize = resize_nearest(img, (small_width, small_height))   
show({
    f"pyrDown x{down_steps}": small_pyr,
    "resize": small_resize,
    "difference x3": difference(small_pyr, small_resize, 3),
})


## 2. Ampliar x2: pyrUp frente a resize al doble de tamaño
big_pyr = upscale_pyr(img, 1)
big_height, big_width = big_pyr.shape
big_resize = resize_nearest(img, (big_width, big_height))
show({
    "pyrUp": big_pyr,
    "resize": big_resize,
    "difference x5": difference(big_pyr, big_resize, 5),
})


## 3. Ida y vuelta: comprobar la información que se pierde al reducir con la pirámide no se puede recuperar al volver a ampliar.
steps = 2
round_trip = upscale_pyr(downscale_pyr(img, steps), steps)
round_trip = fix_size(round_trip, height, width)   # la vuelta puede salir más grande que img
show({
    "original": img,
    "round trip": round_trip,
    "difference x5": difference(img, round_trip, 5),
})
