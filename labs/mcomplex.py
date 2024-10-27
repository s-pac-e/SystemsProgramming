import math

class mcomplex:
    def __init__(self, r: int, i: int):
        """
        Initialize an mcomplex object and its data attributes
        """
        self.__update(r, i)

    def __update(self, r: int = 0, i: int = 0):
        """
        Update the data attributes of this mcomplex object. (Private method)
        Must include real part, imaginary part, and the distance magnitude.
        """
        self.r = r  # Real part
        self.i = i  # Imaginary part
        self.d = math.sqrt(r**2 + i**2)  # Distance magnitude

    def print(self):
        print(f"{self.r} + {self.i}i")

    def __add__(self, other) -> 'mcomplex':
        """
        :return: (a + bi) + (c + di) = (a + c) + (b + d)i
        """
        return mcomplex(self.r + other.r, self.i + other.i)

    def __sub__(self, other) -> 'mcomplex':
        """
        Calculate and return the subtraction of two mcomplex objects.
        :return: (a + bi) - (c + di) = (a - c) + (b - d)i
        """
        return mcomplex(self.r - other.r, self.i - other.i)

    def __mul__(self, other) -> 'mcomplex':
        """
        Calculate and return the multiplication of two mcomplex objects.
        :return: (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        """
        real_part = self.r * other.r - self.i * other.i
        imag_part = self.r * other.i + self.i * other.r
        return mcomplex(real_part, imag_part)

    def __truediv__(self, other) -> 'mcomplex':
        """
        Calculate and return the division of two mcomplex objects.
        :return: (a + bi) / (c + di) = ((ac + bd) + (bc - ad)i) / (c^2 + d^2)
        """
        denominator = other.r**2 + other.i**2
        real_part = (self.r * other.r + self.i * other.i) / denominator
        imag_part = (self.i * other.r - self.r * other.i) / denominator
        return mcomplex(real_part, imag_part)

    def __eq__(self, other) -> bool:
        """
        Compare whether two mcomplex objects are equal.
        Return True if both mcomplex objects are the same, False otherwise.
        """
        return self.r == other.r and self.i == other.i

    def __ne__(self, other) -> bool:
        """
        Compare whether two mcomplex objects are not equal.
        Return True if both mcomplex objects are not the same, False otherwise.
        """
        return not self.__eq__(other)

    def __lt__(self, other) -> bool:
        """
        Calculate whether the first mcomplex number is less than the second one
        based on the magnitude and return True, otherwise return False.
        :return: self < other ?
        """
        return self.d < other.d

    def __gt__(self, other) -> bool:
        """
        Calculate whether the first mcomplex number is greater than the second one
        based on the magnitude and return True, otherwise return False.
        :return: self > other ?
        """
        return self.d > other.d

    def test():
        # Sample test code
        c1 = mcomplex(3, 4)
        c2 = mcomplex(1, 2)
        print("Addition:", (c1 + c2).print())
        print("Subtraction:", (c1 - c2).print())
        print("Multiplication:", (c1 * c2).print())
        print("Division:", (c1 / c2).print())
        print("Equal:", c1 == c2)
        print("Not Equal:", c1 != c2)
        print("Less than:", c1 < c2)
        print("Greater than:", c1 > c2)

if __name__ == "__main__":
    mcomplex.test()
