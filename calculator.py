class Calculator:
    @staticmethod
    def add(x: float, y: float) -> float:
        return x + y

    @staticmethod
    def subtract(x: float, y: float) -> float:
        return x - y

    @staticmethod
    def multiplication(x: float, y: float) -> float:
        return x * y

    @staticmethod
    def division(x: float, y: float) -> float:
        if y==0:
            raise ValueError("Cannot divide by error")
        return x // y


# cal = Calculator()
#
# print(cal.add(5, 15))
# print(cal.subtract(25, 10))
# print(cal.multiplication(5, 8))
# print((cal.division(100, 20)))
