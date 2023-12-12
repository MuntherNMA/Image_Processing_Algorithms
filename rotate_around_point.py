import cv2
import sys
import numpy as np

input_path = sys.argv[1]
output_path = sys.argv[2]

img = cv2.imread(input_path)
rows, cols = img.shape[:2]

rotation_point = (100, 100) 
M = cv2.getRotationMatrix2D(rotation_point, 30, 1)
rotated_img = cv2.warpAffine(img, M, (cols, rows))

cv2.imwrite(output_path, rotated_img)