import math


class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.__denominator = denominator
        self.__normalise()

    @property
    def numeratot(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __str__(self):
        return f'{self.numerator} / {self.denominator}'

    def __mul__(self, other: 'Rational') -> 'Rational':
        return Rational(self.numerator * other.__numerator, self.__denominator * other.__denominator)

    def __floordiv__(self, other: 'Rational'):
        return Rational(self.__numerator * other.__denominator, self.__denominator * other.__numerator)

    def __add__(self, other: 'Rational') -> 'Rational':
        newnum = self.__numerator * other.__denominator + self.__denominator * other.__numerator
        newden = self.__denominator * other.__denominator
        return Rational(newnum, newden)

    def __sub__(self, other: 'Rational') -> 'Rational':
        newnum = self.__numerator * other.__denominator - self.__denominator * other.__numerator
        newden = self.__denominator * other.__denominator
        return Rational(newnum, newden)

    def __lt__(self, other: 'Rational'):
        return self.__numerator / self.__denominator < other.__numerator / other.__denominator

    def __le__(self, other: 'Rational'):
        return self.__numerator / self.__denominator <= other.__numerator / other.__denominator

    def __eq__(self, other: 'Rational'):
        return self.__numerator / self.__denominator == other.__numerator / other.__denominator

    def __ne__(self, other: 'Rational'):
        return self.__numerator / self.__denominator != other.__numerator / other.__denominator

    def __gt__(self, other: 'Rational'):
        return self.__numerator / self.__denominator > other.__numerator / other.__denominator

    def __ge__(self, other: 'Rational'):
        return self.__numerator / self.__denominator >= other.__numerator / other.__denominator

    def __normalise(self):
        if self.__denominator < 0 and self.__numerator < 0 or self.denominator < 0:
            self.__numerator *= -1
            self.__denominator *= -1




 