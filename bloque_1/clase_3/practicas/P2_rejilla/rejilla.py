import cv2
import numpy as np

IMAGE = "../data/chessboard.png"
WINDOW = "P2 grid"


def nothing(value):
    pass


def find_lines(edges, rho_res, theta_res, votes, min_theta, max_theta):
    """Rectas de la imagen de bordes con cv2.HoughLines.

    Args:
        edges: imagen de bordes (uint8, 0 o 255).
        rho_res: tamaño de las celdas del acumulador en rho, en píxeles.
        theta_res: tamaño de las celdas del acumulador en theta, en radianes.
        votes: píxeles de borde que necesita una recta para aceptarla.
        min_theta, max_theta: rango de theta de las rectas que se buscan, en radianes.

    Returns:
        Lista de rectas (rho, theta) como float de Python, ordenadas por votos: primero la más votada.
        Vacía si no encuentra ninguna.
    """
    ## TODO: CODE HERE
    lines = []
    ## END TODO
    return lines


def draw_line(img, rho, theta, color):
    """Dibuja sobre img la recta x cos(theta) + y sin(theta) = rho, de borde a borde.

    Args:
        img: imagen sobre la que se dibuja, en color (BGR).
        rho: distancia de la recta al origen (0, 0), en píxeles.
        theta: ángulo de la normal de la recta, en radianes.
        color: color de la recta, en BGR.
    """
    ## TODO: CODE HERE
    ## END TODO


def crossing(line1, line2):
    """Punto de cruce de dos rectas, con cv2.solve.

    Args:
        line1, line2: rectas (rho, theta), como las de find_lines.

    Returns:
        El cruce (x, y), o None si las rectas son paralelas.
    """
    ## TODO: CODE HERE
    point = None
    ## END TODO
    return point


## Cargar la imagen: en color para dibujar encima, en escala de grises para buscar los bordes
img = cv2.imread(IMAGE)
if img is None:
    print("Error: could not read the image")
    exit(1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height, width = gray.shape


## Trackbars
# WINDOW_NORMAL + resizeWindow: las ventanas empiezan a la mitad del tamaño de la foto y se pueden agrandar
# con el ratón (con GTK, nunca por debajo del tamaño que tienen al mostrar la imagen por primera vez)
cv2.namedWindow(WINDOW, cv2.WINDOW_NORMAL)
cv2.namedWindow("edges", cv2.WINDOW_NORMAL)
cv2.resizeWindow(WINDOW, width // 2, height // 2 + 280)     # + 280: las 5 trackbars van dentro de la ventana
cv2.resizeWindow("edges", width // 2, height // 2)
cv2.createTrackbar("canny low", WINDOW, 50, 500, nothing)    # Canny: umbral bajo, los bordes débiles pegados a uno fuerte se quedan
cv2.createTrackbar("canny high", WINDOW, 150, 500, nothing)  # Canny: umbral alto, por encima es borde seguro
cv2.createTrackbar("rho res", WINDOW, 10, 200, nothing)   # tamaño de las celdas del acumulador en rho, en décimas de px
cv2.createTrackbar("theta res", WINDOW, 10, 50, nothing)  # tamaño de las celdas del acumulador en theta, en décimas de grado
cv2.createTrackbar("votes", WINDOW, 350, 3000, nothing)    # píxeles de borde que necesita una recta para aceptarla
cv2.setTrackbarMin("rho res", WINDOW, 1)
cv2.setTrackbarMin("theta res", WINDOW, 1)
cv2.setTrackbarMin("votes", WINDOW, 1)

while True:
    rho_res = cv2.getTrackbarPos("rho res", WINDOW) / 10                        # de décimas de px a px
    theta_res = np.deg2rad(cv2.getTrackbarPos("theta res", WINDOW) / 10)   # de décimas de grado a radianes
    votes = cv2.getTrackbarPos("votes", WINDOW)
    canny_low = cv2.getTrackbarPos("canny low", WINDOW)
    canny_high = cv2.getTrackbarPos("canny high", WINDOW)
    result = img.copy()

    ## 1. Bordes
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, canny_low, canny_high)
    edges = cv2.dilate(edges, None)

    ## 2. Rectas. theta es el ángulo de la normal de la recta: 0 para una recta vertical, 90 grados para una horizontal
    vertical = find_lines(edges, rho_res, theta_res, votes, -np.pi / 4, np.pi / 4)          # theta de -45 a 45 grados
    horizontal = find_lines(edges, rho_res, theta_res, votes, np.pi / 4, 3 * np.pi / 4)     # theta de 45 a 135 grados
    if not isinstance(vertical, list) or not isinstance(horizontal, list):
        print("Error: find_lines must return a list of (rho, theta), see its docstring")
        exit(1)
    for rho, theta in vertical + horizontal:
        draw_line(result, rho, theta, (0, 0, 255))

    ## 3. Cruces: cada recta vertical con cada horizontal, solo los que caen dentro de la imagen
    crossings = []
    for v in vertical:
        for h in horizontal:
            point = crossing(v, h)
            if point is not None and 0 <= point[0] < width and 0 <= point[1] < height:
                crossings.append(point)
    for x, y in crossings:
        cv2.circle(result, (int(x), int(y)), 6, (255, 255, 0), -1)

    cv2.imshow("edges", edges)
    cv2.imshow(WINDOW, result)
    cv2.setWindowTitle(WINDOW, f"vertical: {len(vertical)}   horizontal: {len(horizontal)}   crossings: {len(crossings)}")
    if cv2.waitKey(30) == 27:
        break

cv2.destroyAllWindows()
