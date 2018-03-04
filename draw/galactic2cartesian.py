from numpy import sin, cos


class GalacticToCartesian:
    __x = []
    __y = []
    __z = []
    __ra = []
    __de = []

    def __init__(self, step=100):
        self.step = step

    def append(self, ra, dec):
        x, y, z = self.convert(ra, dec)
        self.__ra.append(ra)
        self.__de.append(dec)
        self.__x.append(x)
        self.__y.append(y)
        self.__z.append(z)

    @classmethod
    def convert(cls, ra, dec):
        return cos(ra) * sin(dec), sin(ra) * sin(dec), cos(dec)

    @property
    def x(self):
        return self.__x[::self.step]

    @property
    def y(self):
        return self.__y[::self.step]

    @property
    def z(self):
        return self.__z[::self.step]

    @property
    def ra(self):
        return self.__ra[::self.step]

    @property
    def de(self):
        return self.__de[::self.step]

    def __len__(self):
        return len(self.__x)