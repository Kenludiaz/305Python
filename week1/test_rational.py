from rational import *

def setup_function():
    Rational._gcd_helper = lambda a, b: 1

def teardown_function():
    Rational._gcd_helper = None

def test_1_2_standard_form():
    original = Rational(1,2)
    standard = Rational(1,2)
    assert standard.equals(original.standard_form())

def test_0_1_standard_form():
    original = Rational(0,1)
    standard = Rational(0,1)
    assert standard.equals(original.standard_form())

def test_n1_1_standard_form():
    original = Rational(-1,1)
    standard = Rational(-1,1)
    assert standard.equals(original.standard_form())

def test_1_n1_standard_form():
    original = Rational(1,-1)
    standard = Rational(-1,1)
    assert standard.equals(original.standard_form())

def test_0_n1_standard_form():
    original = Rational(0, -1)
    standard = Rational(0,1)
    assert standard.equals(original.standard_form())

def test_n1_n1_standard_form():
    original = Rational(-1,-1)
    standard = Rational(1,1)
    assert standard.equals(original.standard_form())

def test_n27_n9_standard_from():
    Rational._gcd_helper = lambda a, b: 9
    original = Rational(27, 9)
    standard = Rational(-27,-9)
    assert standard.equals(original.standard_form())

def test_n4_24_standard_from():
    Rational._gcd_helper = lambda a, b: 4
    original = Rational(-4, 24)
    standard = Rational(4, -24)
    assert standard.equals(original.standard_form())
