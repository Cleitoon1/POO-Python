from unittest.case import TestCase
def anagrama(a):
    if a == a[::-1]:
        return True
    print(a)
    return False

class SomaTest(TestCase):
    def test_anagrama(self):
        self.assertTrue('e', anagrama('e'))
        self.assertTrue('a', anagrama('a'))
        self.assertTrue('a', anagrama('a'))
        self.assertTrue('a', anagrama('a'))
        self.assertTrue('ba', anagrama('ab'))
        self.assertTrue('ab', anagrama('ba'))
        self.assertTrue('a', anagrama('ba'))

