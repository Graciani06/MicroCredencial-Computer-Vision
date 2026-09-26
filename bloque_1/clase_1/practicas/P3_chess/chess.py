import sys

import cv2
import numpy as np


def createChessboard(rows, cols, square_size):
    if rows % square_size != 0 or cols % square_size != 0:
        print("Error: The chessboard size is not a multiple of the square size.")
        sys.exit(1)

    img = np.full((rows, cols, 3), (255, 255, 255), dtype=np.uint8)

    # TODO: recorrer la imagen de casilla en casilla y pintar de negro las que
    # correspondan, hasta formar el patron de tablero.

    return img


if len(sys.argv) < 4:
    print(f"Usage: {sys.argv[0]} <rows> <cols> <square_size>")
    sys.exit(1)
rows = int(sys.argv[1])
cols = int(sys.argv[2])
square_size = int(sys.argv[3])
img = createChessboard(rows, cols, square_size)
cv2.imwrite("chessboard.png", img)
cv2.imshow("Chessboard", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
