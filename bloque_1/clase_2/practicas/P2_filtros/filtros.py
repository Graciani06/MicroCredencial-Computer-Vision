import cv2
import numpy as np

IMAGE = "../data/dog.jpg"
WINDOW = "P2 filters"
NOISE_NAMES = {
    0: "none",
    1: "gaussian",
    2: "salt and pepper"
}
FILTER_NAMES = {
    0: "none",
    1: "box",
    2: "gauss",
    3: "median",
    4: "bilateral"
}


def add_noise(img, noise_type, level):
    """Añade a img el ruido elegido en el trackbar noise (ver NOISE_NAMES).

    - 0: sin ruido, devuelve img sin cambios.
    - 1: ruido gaussiano aditivo de media 0 y desviación típica = level.
    - 2: sal y pimienta en el % = level de los píxeles, elegidos al azar: la mitad pasan a negro (0) y la
      otra mitad a blanco (255).

    Los números aleatorios tienen que salir del generador de OpenCV, el que fija setRNGSeed.

    Args:
        img: imagen de entrada, en escala de grises (uint8).
        noise_type: tipo de ruido: 0, 1 o 2.
        level: gaussiano: desviación típica, en niveles de gris / sal y pimienta: % de píxeles.

    Returns:
        La imagen con ruido, en uint8.
    """
    ## TODO: CODE HERE
    result = img.copy()
    ## END TODO
    return result


def apply_filter(img, filter_type, ksize, sigma_color, sigma_space):
    """Aplica a img el filtro elegido en el trackbar filter (ver FILTER_NAMES).

    - 0: ninguno, devuelve img sin cambios.
    - 1: box: cada píxel pasa a ser la media de su ventana de ksize x ksize.
    - 2: gauss: filtro gaussiano con una ventana de ksize x ksize.
    - 3: mediana: cada píxel pasa a ser la mediana de su ventana de ksize x ksize.
    - 4: bilateral: suaviza respetando los bordes, con sigma_color y sigma_space.

    Gauss y mediana solo admiten un ksize impar: con un ksize par no se aplican y devuelve img sin cambios.

    Args:
        img: imagen de entrada.
        filter_type: tipo de filtro: 0, 1, 2, 3 o 4.
        ksize: tamaño de la ventana.
        sigma_color: bilateral: cuánto pueden diferir en intensidad los vecinos que se promedian.
        sigma_space: bilateral: cuánto pesan los vecinos según su distancia.

    Returns:
        La imagen filtrada.
    """
    ## TODO: CODE HERE
    result = img.copy()
    ## END TODO
    return result


def noise_changed(value):
    """OpenCV la llama cada vez que se mueve el trackbar noise."""
    print(f"Noise changed to {NOISE_NAMES.get(value, 'unknown')}")


def filter_changed(value):
    """OpenCV la llama cada vez que se mueve el trackbar filter."""
    print(f"Filter changed to {FILTER_NAMES.get(value, 'unknown')}")


def k_changed(value):
    """OpenCV la llama cada vez que se mueve el trackbar k."""
    if value % 2 == 0:
        print(f"k = {value} (even: gauss and median are not applied)")
    else:
        print(f"k = {value}")


def nothing(value):
    pass


img = cv2.imread(IMAGE, cv2.IMREAD_GRAYSCALE)
if img is None:
    print("Error: could not read the image")
    exit(1)
img = cv2.pyrDown(img)   # reducir a la mitad


## Trackbars
cv2.namedWindow(WINDOW)
cv2.createTrackbar("noise", WINDOW, 1, 2, noise_changed)    # ver NOISE_NAMES
cv2.createTrackbar("level", WINDOW, 20, 100, nothing)       # gaussiano: desviación típica / sal y pimienta: % de píxeles
cv2.createTrackbar("filter", WINDOW, 1, 4, filter_changed)  # ver FILTER_NAMES
cv2.createTrackbar("k", WINDOW, 5, 15, k_changed)           # tamaño del kernel (ventana de k x k píxeles)
cv2.createTrackbar("sigmaColor", WINDOW, 75, 200, nothing)  # solo bilateral
cv2.createTrackbar("sigmaSpace", WINDOW, 5, 50, nothing)    # solo bilateral
# Minimum values for the trackbars
cv2.setTrackbarMin("k", WINDOW, 1)
cv2.setTrackbarMin("sigmaColor", WINDOW, 1)
cv2.setTrackbarMin("sigmaSpace", WINDOW, 1)

while True:
    noise_type = cv2.getTrackbarPos("noise", WINDOW)
    level = cv2.getTrackbarPos("level", WINDOW)
    filter_type = cv2.getTrackbarPos("filter", WINDOW)
    ksize = cv2.getTrackbarPos("k", WINDOW)
    sigma_color = cv2.getTrackbarPos("sigmaColor", WINDOW)
    sigma_space = cv2.getTrackbarPos("sigmaSpace", WINDOW)

    cv2.setRNGSeed(0)
    noisy = add_noise(img, noise_type, level)
    filtered = apply_filter(noisy, filter_type, ksize, sigma_color, sigma_space)

    # Gauss y mediana solo admiten un tamaño impar: avisar cuando no se aplican
    warning = ""
    if filter_type in (2, 3) and ksize % 2 == 0:
        warning = "   |   WARNING: even k, filter not applied"

    cv2.imshow(WINDOW, cv2.hconcat([noisy, filtered]))
    cv2.setWindowTitle(WINDOW, f"noisy: {cv2.PSNR(img, noisy):.1f} dB   |   filtered: {cv2.PSNR(img, filtered):.1f} dB{warning}")
    if cv2.waitKey(30) == 27:
        break

cv2.destroyAllWindows()
