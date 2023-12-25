import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self): #4
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self): #1
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    
    def test_isupper2(self): #2
        self.assertFalse('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self): #3
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world','4'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()