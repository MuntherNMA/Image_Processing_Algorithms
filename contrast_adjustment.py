import cv2
import numpy as np
import sys

input_path = sys.argv[1]
output_path = sys.argv[2]

img = cv2.imread(input_path)
alpha = 1.5  # Contrast control (1.0-3.0)
adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=0)

cv2.imwrite(output_path, adjusted)