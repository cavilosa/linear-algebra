class Vector:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def __str__(self):
        return "Vector: {}".format(self.coordinates)

v = Vector([8,-9])
w = Vector([1,3])

print v.plus(w)
