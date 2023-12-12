import cv2
import sys
import numpy as np

input_path = sys.argv[1]
output_path = sys.argv[2]

img = cv2.imread(input_path)
result = cv2.addWeighted(img, 0.9, np.zeros(img.shape, img.dtype), 0, 10)  # Increase Red channel intensity

cv2.imwrite(output_path, result)