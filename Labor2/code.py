# -*- coding: utf-8 -*-
import os
import cv2

def readImgSlice(pfad, stufen_koordinaten, outdir="D:/KI_Kamera/Teilstuecke"):
    os.makedirs(outdir, exist_ok=True)
    img = cv2.imread(pfad)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    for i, (y1, y2, x1, x2) in enumerate(stufen_koordinaten):
        stufe = gray[y1:y2, x1:x2]
        dateiname = os.path.join(outdir, f"stufe_{i+1}.png")
        cv2.imwrite(dateiname, stufe)
        print(f"Gespeichert: {dateiname}")

    print("Alle Teilbilder wurden gespeichert.")


cap = cv2.VideoCapture(0)
print("Kamera geöffnet:", cap.isOpened())

ret, frame = cap.read()
filename = "D:/KI_Kamera/greyscale.png"

if ret:
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    cv2.imwrite(filename, frame)
    print(f"Originalbild gespeichert: {filename}")
else:
    print("Kein Frame vorhanden.")
    cap.release()
    exit()

koordinaten = [
    (100, 400, 0, 80),
    (100, 400, 110, 200),
    (100, 400, 280, 400),
    (100, 400, 410, 500),
    (100, 400, 550, 620)
]

readImgSlice(filename, koordinaten)
cap.release()
