"""Comprobación del entorno: versión de OpenCV y NumPy."""
import cv2
import numpy as np

print(f"OpenCV (Python): {cv2.__version__}")
print(f"NumPy: {np.__version__}")

img = np.full((240, 640, 3), 40, dtype=np.uint8)
cv2.putText(img, f"Entorno OK - OpenCV {cv2.__version__}", (20, 130),
            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

import os
if os.environ.get("DISPLAY"):
    cv2.imshow("check", img)
    cv2.waitKey(0)
else:
    cv2.imwrite("check.png", img)
    print("Sin DISPLAY: imagen guardada en check.png")
