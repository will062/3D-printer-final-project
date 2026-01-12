import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame=cap.read()

    print(f"Frame shape: {frame.shape}")
    cv.imshow('Live Camera Feed', frame)
    Z=frame.reshape((-1,3))
    Z=np.float32(Z)
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K=8
    ret, label, center = cv.kmeans(Z, K, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((frame.shape))

    cv.imshow('Quantized Feed', res2)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()