import cv2
import sys
import numpy as np

input_path = sys.argv[1]
output_path = sys.argv[2]

img = cv2.imread(input_path)
# Increase Blue channel intensity for a cooler effect
result = cv2.addWeighted(img, 0.9, np.zeros(img.shape, img.dtype), 0, -10)

cv2.imwrite(output_path, result)