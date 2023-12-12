import cv2
import sys

input_path = sys.argv[1]
output_path = sys.argv[2]

img = cv2.imread(input_path)
flipped_img = cv2.flip(img, 0)

cv2.imwrite(output_path, flipped_img)