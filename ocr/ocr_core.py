try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import nltk
import numpy as np
import cv2


def ocr_core(filename):
    """
    This function will handle the core OCR processing of Image.
    """
    # text = pytesseract.image_to_string(Image.open(filename))

    text = pytesseract.image_to_string(Image.open(filename))
    return text


def cvToPil(cvImage):
    pilImage = Image.fromarray(cvImage)
    return pilImage


def correct_skew(img):
    image = cv2.imread(img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    th, thresh = cv2.threshold(
        gray, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    # cv2.imwrite("bw.png", thresh)

    coords = np.column_stack(np.where(thresh > 0))
    # ang = cv2.minAreaRect(coords)[-1]
    # if ang < -45:
    #     ang = -(90 + ang)
    # else:
    #     ang = -ang
    ang = -1.0*getSkewAngle(image)

    (h, w) = image.shape[:2]
    center = (w//2, h//2)

    M = cv2.getRotationMatrix2D(center, ang, 1.0)
    rotated = cv2.warpAffine(thresh, M, (image.shape[1], image.shape[0]))

    hist = cv2.reduce(rotated, 1, cv2.REDUCE_AVG).reshape(-1)
    th = 2
    H, W = rotated.shape[:2]
    uppers = [y for y in range(H-1) if hist[y] <= th and hist[y+1] > th]
    lowers = [y for y in range(H-1) if hist[y] > th and hist[y+1] <= th]

    rotated = cv2.cvtColor(rotated, cv2.COLOR_GRAY2BGR)
    for y in uppers:
        cv2.line(rotated, (0, y), (W, y), (255, 0, 0), 1)
    for y in lowers:
        cv2.line(rotated, (0, y), (W, y), (0, 255, 0), 1)
    cv2.imwrite("test.png", rotated)
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
            images.append(image[upper[i]-1:lower[i]+2, 0:w])
    return images


def getSkewAngle(cvImage) -> float:
    # Prep image, copy, convert to gray scale, blur, and threshold
    newImage = cvImage.copy()
    gray = cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    thresh = cv2.threshold(
        blur, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Apply dilate to merge text into meaningful lines/paragraphs.
    # Use larger kernel on X axis to merge characters into single line, cancelling out any spaces.
    # But use smaller kernel on Y axis to separate between different blocks of text
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
    dilate = cv2.dilate(thresh, kernel, iterations=5)

    # Find all contours
    contours, hierarchy = cv2.findContours(
        dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # Find largest contour and surround in min area box
    largestContour = contours[0]
    minAreaRect = cv2.minAreaRect(largestContour)

    # Determine the angle. Convert it to the value that was originally used to obtain skewed image
    angle = minAreaRect[-1]
    if angle < -45:
        angle = 90 + angle
    return -1.0 * angle


def removeNoneEnglish(text):
    words = set(nltk.corpus.words.words())
    text = text.split('\n')
    for line in text:
        res = " ".join(w for w in nltk.wordpunct_tokenize(line)
                       if w.lower() in words or not w.isalpha())
        print(res)


# img = cv2.imread("./static/receipts/test3.jpg")
# text = ocr_core(img)
# print(text)
# removeNoneEnglish(text)
