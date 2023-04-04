import kivy
import cv2
import numpy as np

from kivy.app import App
from kivy.uix.button import Button
kivy.require('1.0.6') # replace with your current kivy version !

class MyApp(App):
    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)

    # Получение потока с камеры
    cap = cv2.VideoCapture(0)

    while True:
        # Чтение кадра
        ret, frame = cap.read()

        # Преобразование цветового пространства в HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Создание маски зеленого цвета
        mask = cv2.inRange(hsv, green_lower, green_upper)

        # Нахождение контуров
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Отображение контуров на кадре
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 500:
                cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)

        # Отображение кадра с контурами
        cv2.imshow('frame', frame)

        # Выход из цикла при нажатии клавиши 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Остановка потока с камеры и закрытие окон
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    MyApp().run()