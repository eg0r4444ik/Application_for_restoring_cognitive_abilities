import time

import schedule
import cv2
import numpy as np


# Получение потока с камеры
cap = cv2.VideoCapture(0)

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
    t1 = time.time()
    ret, frame = cap.read()
    for i in range(0, len(frame), 5):
        for j in range(0, len(frame[i]), 5):
            cell = frame[i][j]
            if f(cell[2], cell[1], cell[0]):
                cell[0] = 255
                cell[1] = 1
                cell[2] = 1
    cv2.imshow('frame', frame)


    # Отображение кадра с контурами
    # cv2.imshow('frame', frame)

    # Выход из цикла при нажатии клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    print(time.time() - t1)

# Остановка потока с камеры и закрытие окон
cap.release()
cv2.destroyAllWindows()

