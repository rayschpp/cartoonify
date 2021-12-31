
import cv2
import numpy as np

# const
numRuns = 5

# reading image
img = cv2.imread("./image.jpg")

for _ in range(numRuns):
    print("[" + str(_) + "/" + str(numRuns) + "]")
    # edges
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # cartoonization
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    img = cartoon

imghsv = cv2.cvtColor(cartoon, cv2.COLOR_BGR2HSV).astype("float32")
imghsv[...,2] = imghsv[...,2]*0.5
imghsv[...,1] = imghsv[...,1]*2
cartoon = cv2.cvtColor(imghsv.astype("uint8"), cv2.COLOR_HSV2BGR)

cv2.imwrite("cartoon.png", cartoon)
