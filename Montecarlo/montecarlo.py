import numpy as np
from random import random

class Rectangle():
    def __init__(self, origin_x, origin_y, length, width):
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.length = length
        self.width = width

class MonteCarlo:
    def __init__(self, length, width, rectangles):
        """constructor
        :param length - length of the enclosing rectangle
        :param width - width of the enclosing rectangle
        :param rectangles - array that contains the embedded rectangles
        :raises ValueError if any of the paramters is None
        """
        if length is None or width is None or rectangles is None:
            raise ValueError("You donkey! param can't be None!")

        self.length = length
        self.width = width
        self.rectangles = rectangles # list of objects

    def area(self, num_of_shots):
        """Method "area "to estimate the area of the enclosing rectangle that is not covered by the embedded rectangles
        :param num_of_shots - Number (>0) of generated random points whose location (inside/outside) is analyzed
        :return float
        :raises ValueError if any of the paramters is None
        """
        if num_of_shots is None:
            raise ValueError("You Donkey! Param can't be none.")

        encl_rect = np.arange(self.width * self.length).reshape(self.width, self.length)
        whole_set = list()

        # create the set of points of embedded rectangles
        for rect in self.rectangles:
            start_y = int(rect.origin_y)
            start_x = int(rect.origin_x)
            end_y = int(start_y + rect.width)
            end_x = int(start_x + rect.length)
            rect_set = (encl_rect[start_y:end_y, start_x:end_x]).flatten()

            for point in rect_set.tolist():
                whole_set.append(point)

        points_in = 0

        # compare set of points from embedded rectangles
        # with value of point
        for _ in range(num_of_shots):
            x = int(np.random.uniform() * self.length)
            y = int(np.random.uniform() * self.width)

            if self.inside(x,y, whole_set):
                points_in += 1

        # Monte Carlo area
        area_enclosing = self.length * self.width
        area = area_enclosing * (points_in/num_of_shots)
        area_enclosing -= area

        return area_enclosing

    def inside(self, x, y, rect):
        """Method "inside" to determine if a given point (x,y) is inside a given rectangle
        :param x,y - coordinates of the point to check
        :param rect - given rectangle
        :return bool
        :raises ValueError if any of the paramters is None
        """
        if x is None or y is None or rect is None:
            raise ValueError("You Donkey!")

        encl_rect = np.arange(self.width * self.length).reshape(self.width, self.length)
        whole_set = rect

        point = (encl_rect[y, x]) # for instance for coordinates (0,0) point=0

        # compare the two set of points
        found = False
        if point in whole_set:
            found = True

        return found

if __name__ == "__main__":
    rect1 = Rectangle(0.0, 0.0, 1.0, 2.0)
    rect2 = Rectangle(7.0, 1.0, 3.0, 4.0)
    rects = [rect1, rect2]

    # length, width, tiny rectangles
    mc = MonteCarlo(10,5, rects)
    area = mc.area(100000)  # for 10000 random points the estimated area should already be close to the correct result of 36
    print(area)

    # print("Area of two embedded rectangles (1x2 and 3x4) is " + str(area))
    # if (area > 30 and area < 40):