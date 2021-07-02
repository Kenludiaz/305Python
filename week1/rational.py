from typing import Callable

class Rational:
    numerator: int
    denominator: int

    def __init__(self, numerator: int, denominator: int) -> None:
        _gcd_helper: Callable[[int, int], int] = None
        if denominator == 0:
            raise Exception
        self.numerator = numerator
        self.denominator = denominator

    def equals(self, other: object) -> bool:
        if (isinstance(other, Rational)):
            return (self.denominator == other.denominator) and (self.numerator == other.numerator)
        return False

    def standard_form(self)-> 'Rational':
        """ Returns an equivalent Rational in standard form.
        The standard, or canonical, form of a Rational has a 
        positive denominator
        and the numerator and denominator
        are coprime 
        --  their 
        greatest common factor is 1.
        (Thinking of the rational as a fraction, the fraction
        cannot be reduced/simplified.)
        :return: a new, equivalent Rational in standard form
        """   
        std_numerator = self.numerator
        std_denominator = self.denominator
        """This check helps prevent """
        if std_denominator < 0:
            std_numerator = -std_numerator
            std_denominator = -std_denominator
        divisor = Rational._gcd_helper(std_numerator, std_denominator)
        std_numerator = std_numerator // divisor
        std_denominator = std_denominator // divisor
        return Rational(std_numerator, std_denominator)
        


# def main():
    

# if __name__ == '__main__':
#    main()