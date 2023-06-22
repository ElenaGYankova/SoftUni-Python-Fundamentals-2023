class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        return self.__pi * self.diameter

    def calculate_area(self):
        radius = self.diameter / 2
        return self.__pi * radius ** 2

    def calculate_area_of_sector(self, angle):
        radius = self.diameter / 2
        return (angle / 360) * self.__pi * (radius ** 2)
