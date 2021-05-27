print("Hello World!")

class Rational:
    numerator: int
    denominator: int

    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator = numerator
        self.denominator = denominator

    def equals(self, other: object) -> bool:
        if (isinstance(other, Rational)):
            return (self.denominator == other.denominator) and (self.numerator == other.numerator)
        return False

def main():
    print("Hello World!")
    rational12 = Rational(1, 2)
    rational23 = Rational(2, 3)
    print("Test rational12 equals another Rational(1,2):", "passed" if rational12.equals(Rational(1, 2)) else "failed")
    print("Test rational12 not equals rational23:", "passed" if not rational12.equals(rational23) else "failed")

if __name__ == '__main__':
   main()