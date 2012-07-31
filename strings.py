#!/usr/bin/env python

import ipdb
import unittest

class String(unittest.TestCase):
   
    def test_lower(self):
       self.assertEquals('abcd', 'ABCD'.lower() ) 

    def test_captalize(self):
       self.assertEquals('Abcd', 'abcd'.capitalize() )
   
    def test_center(self):
        self.assertEquals('===center===', 'center'.center(12, '=') )

    def test_count(self):
        self.assertEquals(3, 'aaaiiiaaa'.count('i', 0, 9) )
        self.assertEquals(1, 'aaaiiiaaa'.count('i', 0, 4) )
        self.assertEquals(3, 'aaaiiiaaa'.count('i', 3, 6) )

    def test_encode(self):
        string = 'test'.encode()
        self.assertEquals('str', type(string).__name__ )

    def test_decode(self):
        string = 'test'.decode()
        self.assertEquals('unicode', type(string).__name__ )

    def test_endsWith(self):
        string = 'test_end'
        self.assertTrue( string.endswith('_end') )
        self.assertFalse( string.endswith('test_') )

    def test_expandTabs(self):
        string = 'teste\tteste\t'
        self.assertEquals('teste   teste   ', string.expandtabs() )

    def test_find(self):
        string = "abcdefg" 
        self.assertEquals(3, string.find('d') )
        self.assertEquals(0, string.find('a') )
        self.assertEquals(6, string.find('g') )

    def test_fotmat(self):
        self.assertEquals('[1, 2, 3]', "[{0}, {1}, {2}]".format(1, 2, 3) )
        self.assertEquals('[1, 1, 3]', "[{0}, {0}, {2}]".format(1, 2, 3) )
        
    def test_index(self):
        self.assertEquals(4, 'abcde'.index('e') )
        self.assertEquals(0, 'abcde'.index('a') )
        
    def test_isAlnum(self):
        self.assertFalse( '$%ss#@'.isalnum() )
        self.assertTrue( 'abcde'.isalnum() )

    def test_isAlpha(self):
        self.assertTrue( 'abcd'.isalpha() )
        self.assertFalse( 'abcd.$%%'.isalpha() ) 

    def test_isDigit(self):
        self.assertTrue( '1234'.isdigit() )   
        self.assertFalse( 'a1234'.isdigit() )      

    def test_isLower(self):
        self.assertTrue( 'a'.islower() )
        self.assertFalse( 'A'.islower() )

    def test_isSpace(self):
        self.assertTrue( '  '.isspace() )
        self.assertFalse( ' .... '.isspace() )

    def test_lStrip(self):
        self.assertEquals( 'test',  '-test'.lstrip('-') )

 
if __name__ == '__main__':
    unittest.main()

