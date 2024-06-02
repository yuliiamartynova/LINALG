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

    def universal_transformation_2D(self, matrix):
        x_array = []
        y_array = []

        for i in self.dots:
            x_value = i[0]* matrix[0,0] + i[1] * matrix[0,1]
            y_value = i[0]* matrix[1,0] + i[1] * matrix[1,1]
            x_array.append(x_value)
            y_array.append(y_value)
        return (np.array(x_array), np.array(y_array))

    def universal_transformation_3D(self, matrix):
        x_array = []
        y_array = []
        z_array = []

        for point in self.points:
            x_value = point[0] * matrix[0, 0] + point[1] * matrix[0, 1] + point[2] * matrix[0, 2]
            y_value = point[0] * matrix[1, 0] + point[1] * matrix[1, 1] + point[2] * matrix[1, 2]
            z_value = point[0] * matrix[2, 0] + point[1] * matrix[2, 1] + point[2] * matrix[2, 2]
            x_array.append(x_value)
            y_array.append(y_value)
            z_array.append(z_value)

        return np.array(x_array), np.array(y_array), np.array(z_array)


## фігура сердечка (рівняння з інтернету)
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - np.cos(3*t) - np.cos(4*t)
points_array = np.column_stack((x, y))

heart = Figure(points_array, 'red')

mat = np.array([[1,2], [-1,0]])
##a, b = heart.rotate(360)
## a, b = heart.scale(1/2)
##a,b = heart.reflect(1, -1,0)
##a,b = heart.tilt_y(2)
a,b = heart.universal_transformation_2D(mat)



plt.figure(8, (8,8))
plt.plot(x, y, heart.colour)
plt.grid(True)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()


triangle_dots = np.array([[-7, 10], [4, -11], [5, 20]])
triangle = Figure(triangle_dots, 'black')
c, d = triangle.tilt_x(2)
vertices = triangle_dots
##vertices = np.array(list(zip(c,d)))
# Plot the triangle
plt.fill(vertices[:, 0], vertices[:, 1], 'green')
plt.plot(vertices[:, 0], vertices[:, 1], 'black')
plt.axis('equal')
plt.grid(True)
plt.legend()

plt.show()



