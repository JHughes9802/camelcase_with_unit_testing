import unittest
from unittest import TestCase

import camelcase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):

        self.assertEqual('helloWorld', camelcase.camel_case('Hello World'))
    
    def test_special_characters(self):

        self.assertEqual('!@#$%^&*()', camelcase.camel_case('! @ # $ % ^ & * ( )'))
        self.assertEqual('~`_-+={}[]|\:;', camelcase.camel_case('~ ` _ - + = { } [ ] | \ : ;'))
        self.assertEqual('""\'\'<>,.?/', camelcase.camel_case('" " \' \' < > , . ? /'))
        # Despite output still containing the tabs, words have proper capitalization
        self.assertEqual('tabs\tIn\tBetween', camelcase.camel_case('tAbS\tiN\tbEtWeEn'))

    def test_only_numbers(self):

        self.assertEqual('1234567890', camelcase.camel_case('1 2 3 4 5 6 7 8 9 0'))
    
    def test_leading_and_ending_spaces(self):

        self.assertEqual('test123Hello', camelcase.camel_case('  test 123 hello  '))
    
    def test_all_letters_same_case(self):

        self.assertEqual('thisIsAllCapitalLetters', camelcase.camel_case('THIS IS ALL CAPITAL LETTERS'))
        self.assertEqual('thisIsAllLowercaseLetters', camelcase.camel_case('this is all lowercase letters'))
    
    # def test_trying_to_break_with_keywords(self):

    #     self.assertEqual('"break"')

if __name__ == "__main__":
    unittest.main()