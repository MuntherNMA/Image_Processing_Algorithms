import cv2
import numpy as np
import sys

input_path = sys.argv[1]
output_path = sys.argv[2]

img = cv2.imread(input_path)
brightness_offset = 50  # Adjust this value to change brightness

result = cv2.add(img, np.array([brightness_offset], dtype='uint8'))
cv2.imwrite(output_path, result)