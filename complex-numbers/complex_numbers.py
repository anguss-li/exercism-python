from __future__ import annotations

from math import cos, e, sin, sqrt


class ComplexNumber:
    def __init__(self, real: float, imaginary: float):
        '''
        Define a complex number in the form a + b * i where real == a and 
        imaginary == b
        '''
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other: ComplexNumber) -> bool:
        '''Check if two complex numbers have equal real and imaginary parts'''
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other: ComplexNumber) -> ComplexNumber:
        '''Return sum of self and other'''
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return ComplexNumber(real, imaginary)

    def __mul__(self, other: ComplexNumber) -> ComplexNumber:
        '''Return product of self and other'''
        a, b, c, d = self.real, self.imaginary, other.real, other.imaginary
        real = a*c - b*d
        imaginary = b*c + a*d
        return ComplexNumber(real, imaginary)

    def __sub__(self, other: ComplexNumber) -> ComplexNumber:
        '''Return difference of self and other'''
        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        return ComplexNumber(real, imaginary)

    def __truediv__(self, other: ComplexNumber) -> ComplexNumber:
        '''Return quotient of self and other'''
        a, b, c, d = self.real, self.imaginary, other.real, other.imaginary
        denominator = c**2 + d**2
        real = (a*c + b*d) / denominator
        imaginary = (b*c - a*d) / denominator
        return ComplexNumber(real, imaginary)

    def __abs__(self) -> float:
        '''Return absolute value of self'''
        return sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self) -> ComplexNumber:
        '''Return conjugate of self'''
        return ComplexNumber(self.real, self.imaginary*-1)

    def exp(self) -> ComplexNumber:
        '''Return e to the power of self'''
        a, b = self.real, self.imaginary
        real = e**a * cos(b)
        imaginary = sin(b)
        return ComplexNumber(real, imaginary)
