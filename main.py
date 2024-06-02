import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

class Figure:
    def __init__(self, dots):
        self.dots = dots

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

        for i in self.dots:
            x_value = i[0] * matrix[0, 0] + i[1] * matrix[0, 1] + i[2] * matrix[0, 2]
            y_value = i[0] * matrix[1, 0] + i[1] * matrix[1, 1] + i[2] * matrix[1, 2]
            z_value = i[0] * matrix[2, 0] + i[1] * matrix[2, 1] + i[2] * matrix[2, 2]
            x_array.append(x_value)
            y_array.append(y_value)
            z_array.append(z_value)

        return np.array(x_array), np.array(y_array), np.array(z_array)

## фігура сердечка (рівняння з інтернету)
def create_heart():
    t = np.linspace(0, 2 * np.pi, 1000)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - np.cos(3*t) - np.cos(4*t)
    return np.column_stack((x, y))

def create_triangle():
    triangle_dots = np.array([[-7, 10], [4, -11], [5, 20]])
    return triangle_dots

def drawing_figures(a,b,c,d):
    plt.figure(8, (8, 8))
    plt.plot(a, b, "pink")
    plt.grid(True)
    plt.legend()

    plt.fill(c, d, "yellow")
    plt.axis('equal')
    plt.legend()

    plt.show()

heart = Figure(create_heart())
triangle = Figure(create_triangle())
mat = np.array([[1,3], [2,5]])

a, b = create_heart()[:, 0], create_heart()[:, 1]
##a, b = heart.rotate(360)
## a, b = heart.scale(1/2)
##a,b = heart.reflect(1, -1,0)
##a,b = heart.tilt_y(2)
##a,b = heart.universal_transformation_2D(mat)
c, d = create_triangle()[:, 0], create_triangle()[:, 1]
##c, d = triangle.rotate(90)
## c, d = triangle.scale(1/2)
##c,d = triangle.reflect(1, -1,0)
##c,d = triangle.tilt_y(2)
#c,d = triangle.universal_transformation_2D(mat)
##c, d = triangle.tilt_x(9)
#drawing_figures(a,b,c,d)

vertices = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [0.5, np.sqrt(3)/2, 0],
    [0.5, np.sqrt(3)/6, np.sqrt(2/3)]
])

transformation_matrix = np.array([
    [1, 0, 4],
    [0, 1, 0],
    [0, 0, 1]
])
three_d_figure = Figure(vertices)

x_transformed, y_transformed, z_transformed = three_d_figure.universal_transformation_3D(transformation_matrix)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x_transformed, y_transformed, z_transformed, color='red')
for i in range(len(x_transformed)):
    for j in range(i + 1, len(x_transformed)):
        ax.plot([x_transformed[i], x_transformed[j]], [y_transformed[i], y_transformed[j]], [z_transformed[i], z_transformed[j]], color='red')

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.legend()

plt.show()






