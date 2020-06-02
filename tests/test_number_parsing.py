import pytest
from number_parser import parser

class TestNumberParser():
    def basic_test(self):
        assert parser.parser("two million three thousand nine hundred and eighty four") == 2003984
        assert parser.parser("nineteen") == 19
        assert parser.parser("two thousand and nineteen") == 2019
        assert parser.parser("two million three thousand and nineteen") == 2003019
        assert parser.parser('three billion') == 3000000000
        assert parser.parser('three million') == 3000000
        assert parser.parser('one hundred twenty three million four hundred fifty six thousand seven hundred and eighty nine') == 123456789
        assert parser.parser('eleven') == 11
        assert parser.parser('nineteen billion and nineteen') == 19000000019
        assert parser.parser('one hundred and forty two') == 142
        assert parser.parser('two million twenty three thousand and forty nine') == 2023049
        assert parser.parser('hundred') == 100
        assert parser.parser('thousand') == 1000
        assert parser.parser('million') == 1000000
        assert parser.parser('billion') == 1000000000