import cv2
import numpy as np
import sys

input_path = sys.argv[1]
output_path = sys.argv[2]

img = cv2.imread(input_path)

gamma = 2.2 # Change this value for different results
gamma_inv = 1.0 / gamma
table = np.array([((i / 255.0) ** gamma_inv) * 255 for i in np.arange(0, 256)]).astype("uint8")

img_gamma = cv2.LUT(img, table)

cv2.imwrite(output_path, img_gamma)