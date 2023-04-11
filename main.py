import time
import cv2
import numpy as np


# Получение потока с камеры
cap = cv2.VideoCapture(1)

lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])
lower_red2 = np.array([170,50,50])
upper_red2 = np.array([180,255,255])

def f(r, g, b):
    red_filter = [[150, 255], [0, 120], [0, 120]]
    if not (red_filter[2][0] <= b <= red_filter[2][1]):
        return False
    if not (red_filter[1][0] <= g <= red_filter[1][1]):
        return False
    if not (red_filter[0][0] <= r <= red_filter[0][1]):
        return False
    return True

while True:
    # Чтение кадра
    ret, frame = cap.read()
    # конвертация в формат HSV
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # создание маски для синих пикселей
    lower_blue = (100, 150, 150)
    upper_blue = (140, 255, 255)
    mask3 = cv2.inRange(hsv_img, lower_blue, upper_blue)

    lower_red = np.array([0, 150, 150])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv_img, lower_red, upper_red)

    lower_red = np.array([170, 150, 150])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv_img, lower_red, upper_red)

    # Объединение масок
    mask = mask1 + mask2 + mask3

    # применение маски к изображению
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # отображение изображения
    cv2.imshow('Result', result)

    # Выход из цикла при нажатии клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Остановка потока с камеры и закрытие окон
cap.release()
cv2.destroyAllWindows()

