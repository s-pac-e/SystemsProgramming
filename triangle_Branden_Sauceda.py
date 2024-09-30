import math



class triangle:
    def __init__(self, base: float, height: float):
        self.__base = base
        self.__height = height
        self.__update_attributes()
    
    def __update_attributes(self):
        self.side = self.calc_side()
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()
        self.alpha = self.calc_alpha()
        self.beta = self.calc_beta()

    def set_base(self, base: float):
        if base > 0:
            self.__base = base
            self.__update_attributes()
        else:
            raise ValueError("Base must be greater than 0.")

    def set_height(self, height: float):
        if height > 0:
            self.__height = height
            self.__update_attributes()
        else:
            raise ValueError("Height must be greater than 0.")
    
    def get_base(self) -> float:
        return self.__base
    
    def get_height(self) -> float:
        return self.__height

    def calc_side(self) -> float:
        return math.sqrt((self.__base / 2) ** 2 + self.__height ** 2)

    def calc_perimeter(self) -> float:
        return self.__base + 2 * self.side

    def calc_area(self) -> float:
        return 0.5 * self.__base * self.__height

    def calc_alpha(self) -> float:
        return math.degrees(math.atan(self.__height / (self.__base / 2)))

    def calc_beta(self) -> float:
        return 180 - 2 * self.alpha

    def print_all(self) -> None:
        print(f"------------------------------")
        print(f"base : {self.__base}")
        print(f"height : {self.__height}")
        print(f"side : {self.side}")
        print(f"perimeter: {self.perimeter}")
        print(f"area : {self.area}")
        print(f"alpha : {self.alpha}")
        print(f"beta : {self.beta}")
        print(f"------------------------------")
x = triangle(6,8)
x.print_all()
x.set_base(10)
x.print_all()