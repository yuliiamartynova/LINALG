import matplotlib.pyplot as plt
import numpy as np


class Figure:
    def __init__(self, dots, colour):
        self.dots = dots
        self.colour = colour

    def rotate(self, degree):
        x_array = []
        y_array = []
        a = degree * np.pi /180

        for i in self.dots:
            x_value = (i[0] * np.cos(a)) + (- np.sin(a)) * i[1]
            y_value = np.cos(a) *i[1] + np.sin(a) * i[0]
            x_array.append(x_value)
            y_array.append(y_value)
        return (np.array(x_array), np.array(y_array))

    def scale(self, coef):
        x_array = []
        y_array = []

        for i in self.dots:
            x_value = i[0] * coef
            y_value = i[1] * coef
            x_array.append(x_value)
            y_array.append(y_value)
        return (np.array(x_array), np.array(y_array))

    def reflect(self, a, b, c):
        x_array = []
        y_array = []
        for i in self.dots:
            temp = -2 * (a * i[0] + b * i[1] + c) / (a * a + b * b)
            x_value = temp * a + i[0]
            y_value = temp * b + i[1]
            x_array.append(x_value)
            y_array.append(y_value)
        return (np.array(x_array), np.array(y_array))


    def tilt_x(self, coef):
        x_array = []
        y_array = []

        for i in self.dots:
            x_value = i[0] + i[1]* coef
            y_value = i[1]
            x_array.append(x_value)
            y_array.append(y_value)
        return (np.array(x_array), np.array(y_array))

    def tilt_y(self, coef):
        x_array = []
        y_array = []

        for i in self.dots:
            x_value = i[0]
            y_value = i[0] * coef+i[1]
            x_array.append(x_value)
            y_array.append(y_value)
        return (np.array(x_array), np.array(y_array))

    def universal_transformation(self, matrix):
        return 0

## фігура сердечка (рівняння з інтернету)
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - np.cos(3*t) - np.cos(4*t)
points_array = np.column_stack((x, y))

heart = Figure(points_array, 'red')


##a, b = heart.rotate(360)
## a, b = heart.scale(1/2)
a,b = heart.reflect(1, -1,0)
##a,b = heart.tilt_y(2)

## тут малюю
plt.figure(8, (8,8))
plt.plot(a, b, heart.colour)

plt.grid(True)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()
