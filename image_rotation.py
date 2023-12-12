import cv2
import sys
import numpy as np

input_path = sys.argv[1]
output_path = sys.argv[2]

img = cv2.imread(input_path)
rows, cols = img.shape[:2]

M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
rotated_img = cv2.warpAffine(img, M, (cols, rows))

cv2.imwrite(output_path, rotated_img) 