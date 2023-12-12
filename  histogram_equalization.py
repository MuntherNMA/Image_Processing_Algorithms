import cv2
import sys

input_path = sys.argv[1]
output_path = sys.argv[2]

img = cv2.imread(input_path, 0)
eq_img = cv2.equalizeHist(img)

cv2.imwrite(output_path, eq_img)