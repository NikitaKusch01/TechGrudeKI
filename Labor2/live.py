import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.color import rgb2gray

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kein Frame gelesen.")
        break

    grayscale = rgb2gray(frame)
    plt.imshow(grayscale, cmap=plt.cm.gray)
    plt.title("Grayscale (Fenster schließen zum Beenden)")
    plt.axis('off')
    plt.show()
    break  # verhindert endlose Schleife – zeige nur ein Bild

ret, frame = cap.read()
filename = "D:/KI_Kamera/white_4.png"

if ret:
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(filename, gray)
    print(f"Originalbild gespeichert: {filename}")
else:
    print("Kein Frame vorhanden.")

cap.release()
cv2.destroyAllWindows()
