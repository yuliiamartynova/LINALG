import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("C:/Users/marti/Downloads/froggy.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    translated = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return translated

def rotate(image, angle, scale=1.0):
    center = (image.shape[1] // 2, image.shape[0] // 2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return rotated

def scale(image, fx, fy):
    scaled = cv2.resize(image, None, fx=fx, fy=fy)
    return scaled

def perspective_transform(image, pts1, pts2):
    M = cv2.getPerspectiveTransform(pts1, pts2)
    transformed = cv2.warpPerspective(image, M, (image.shape[1], image.shape[0]))
    return transformed

translated_image = translate(image, 100, 50)
rotated_image = rotate(image, 45)
scaled_image = scale(image, 0.5, 0.5)

pts1 = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250], [240, 200]])
perspective_image = perspective_transform(image, pts1, pts2)

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.title("Original Image")
plt.imshow(image)

plt.subplot(2, 2, 2)
plt.title("Translated Image")
plt.imshow(translated_image)

plt.subplot(2, 2, 3)
plt.title("Rotated Image")
plt.imshow(rotated_image)

plt.subplot(2, 2, 4)
plt.imshow(scaled_image)

plt.figure()
plt.imshow(perspective_image)

plt.show()