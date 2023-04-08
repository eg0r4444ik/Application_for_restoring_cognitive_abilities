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
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask_red = cv2.inRange(hsv, lower_red, upper_red) + cv2.inRange(hsv, lower_red2, upper_red2)
    result = cv2.bitwise_and(frame, frame, mask=mask_red)
    # for i in range(0, len(frame), 5):
    #     for j in range(0, len(frame[i]), 5):
    #         cell = frame[i][j]
    #         if f(cell[2], cell[1], cell[0]):
    #             cell[0] = 255
    #             cell[1] = 1
    #             cell[2] = 1
    # cv2.imshow('frame', frame)
    cv2.imshow('image', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Отображение кадра с контурами
    # cv2.imshow('frame', frame)

    # Выход из цикла при нажатии клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Остановка потока с камеры и закрытие окон
cap.release()
cv2.destroyAllWindows()

