# 1000 M
# 500 D
# 100 C
#  50 L
#  10 X
#   5 V
#   1 I

import pytest


def convert(number):
    values = {"M": 1000,
              "CM": 900,
              "D": 500,
              "CD": 400,
              "C": 100,
              "XC": 90,
              "L": 50,
              "XL": 40,
              "X": 10,
              "IX": 9,
              "V": 5,
              "IV": 4,
              "I": 1}

    conversion = ''
    for roman, arabic in values.items():
        quotient = number // arabic
        conversion += quotient * roman
        number -= quotient * arabic

    return conversion




def test_for_1():
    assert convert(1) == "I"


def test_for_2():
    assert convert(2) == "II"


def test_for_4():
    assert convert(4) == "IV"


def test_for_5():
    assert convert(5) == "V"


def test_for_6():
    assert convert(6) == "VI"


def test_for_9():
    assert convert(9) == "IX"


def test_for_10():
    assert convert(10) == "X"


def test_for_50():
    assert convert(50) == "L"


def test_for_83():
    assert convert(83) == "LXXXIII"


def test_for_99():
    assert convert(99) == "XCIX"

def test_for_100():
    assert convert(100) == "C"


def test_for_400():
    assert convert(400) == "CD"


def test_for_444():
    assert convert(444) == "CDXLIV"


def test_for_1800():
    assert convert(1800) == "MDCCC"


def test_for_3999():
    assert convert(3999) == "MMMCMXCIX"