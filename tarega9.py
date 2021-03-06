from unittest import TestCase
def anagrama(a, b):
    if a.replace(" ", "").upper() == b[::-1].replace(" ", "").upper():
        return True
    return False

class SomaTest(TestCase):
    def test_anagrama(self):
        self.assertTrue(anagrama('', ''))
        self.assertTrue(anagrama(' ', ''))
        self.assertTrue(anagrama('a', 'a '))
        self.assertFalse(anagrama('b', 'a'))
        self.assertTrue(anagrama('a', ' a      '))
        self.assertTrue(anagrama('b a','a b'))
        self.assertTrue(anagrama('ab','ba'))
        self.assertTrue(anagrama('casa', 'asac'))
        self.assertFalse(anagrama('cleiton', 'cadeira'))
        self.assertFalse(anagrama('python', 'java'))
