import numpy as np
import cv2


def correct_skew():
    image = cv2.imread("./receipts/test.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    th, thresh = cv2.threshold(
        gray, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    # cv2.imwrite("bw.png", thresh)

    coords = np.column_stack(np.where(thresh > 0))
    ang = cv2.minAreaRect(coords)[-1]
    if ang < -45:
        ang = -(90 + ang)
    else:
        ang = -ang

    (h, w) = image.shape[:2]
    center = (w//2, h//2)

    M = cv2.getRotationMatrix2D(center, ang, 1.0)
    rotated = cv2.warpAffine(thresh, M, (image.shape[1], image.shape[0]))

    hist = cv2.reduce(rotated, 1, cv2.REDUCE_AVG).reshape(-1)
    th = 2
    H, W = image.shape[:2]
    uppers = [y for y in range(H-1) if hist[y] <= th and hist[y+1] > th]
    lowers = [y for y in range(H-1) if hist[y] > th and hist[y+1] <= th]

    rotated = cv2.cvtColor(rotated, cv2.COLOR_GRAY2BGR)
    for y in uppers:
        cv2.line(rotated, (0, y), (W, y), (255, 0, 0), 1)
    for y in lowers:
        cv2.line(rotated, (0, y), (W, y), (0, 255, 0), 1)
    # cv2.imwrite("test.png", rotated)
    return uppers, lowers, rotated


def cropLine(upper, lower, image):
    av = 0
    for i in range(len(upper)):
        av += lower[i] - upper[i]
    av = av/len(upper)
    print(av)
    w = image.shape[1]
    images = []
    for i in range(len(upper)):
        if lower[i] - upper[i] > av:
            images.append(image[upper[i]:lower[i], 0:w])
    return images


upper, lower, image = correct_skew()
cv2.imwrite("test.png", image)
imgs = cropLine(upper, lower, image)
for i in range(len(imgs)):
    fileN = "test"+str(i)+".png"
    cv2.imwrite(fileN, imgs[i])
