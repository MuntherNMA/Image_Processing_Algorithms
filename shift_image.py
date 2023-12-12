import cv2
import sys
import numpy as np

input_path = sys.argv[1]
output_path = sys.argv[2]

img = cv2.imread(input_path)
rows, cols = img.shape[:2]

M = np.float32([[1, 0, 10], [0, 1, 0]])  # Shift 10 pixels right
shifted_img = cv2.warpAffine(img, M, (cols, rows))

cv2.imwrite(output_path, shifted_img)