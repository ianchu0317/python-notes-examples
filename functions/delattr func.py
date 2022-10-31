class Coord:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def show(self):
        print("Point is ({}{}{})".format(self.x, self.y, self.z))


if __name__ == '__main__':
    p = Coord(2, 4, 5)
    p.show()

    # delete atribute
    delattr(p, 'z')

    p.show()
