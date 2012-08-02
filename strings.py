#!/usr/bin/env python

import ipdb
import unittest

class StringTest(unittest.TestCase):
   
    def test_lower(self):
        """
        Return a copy of the string with all the cased characters [4] converted to lowercase.
        """
        self.assertEquals('abcd', 'ABCD'.lower() ) 

    def test_captalize(self):
        """
        Return a copy of the string with its first character capitalized and the rest lowercased.
        """
        self.assertEquals('Abcd', 'abcd'.capitalize() )
   
    def test_center(self):
        """
        Return centered in a string of length width. Padding is done using the specified 
        fillchar (default is a space). 
        """
        self.assertEquals('===center===', 'center'.center(12, '=') )
        self.assertEquals('===center==',  'center'.center(11, '=') )

    def test_count(self):
        """
        Return the number of non-overlapping occurrences of substring sub in the range [start, end]. 
        Optional arguments start and end are interpreted as in slice notation.
        """
        self.assertEquals(3, 'aaaiiiaaa'.count('i', 0, 9) )
        self.assertEquals(1, 'aaaiiiaaa'.count('i', 0, 4) )
        self.assertEquals(3, 'aaaiiiaaa'.count('i', 3, 6) )

    def test_encode(self):
        """
        Return an encoded version of the string. Default encoding is the current default 
        string encoding. errors may be given to set a different error handling scheme. 
        The default for errors is 'strict', meaning that encoding errors raise a UnicodeError. 
        Other possible values are 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 
        and any other name registered via codecs.register_error(), see section Codec Base 
        Classes. For a list of possible encodings, see section Standard Encodings.
        """
        string = 'test'.encode()
        self.assertEquals('str', type(string).__name__ )

    def test_decode(self):
        """
        Decodes the string using the codec registered for encoding. encoding defaults 
        to the default string encoding. errors may be given to set a different error 
        handling scheme. The default is 'strict', meaning that encoding errors raise 
        UnicodeError. Other possible values are 'ignore', 'replace' and any other name 
        registered via codecs.register_error(), see section Codec Base Classes.
        """
        string = 'test'.decode()
        self.assertEquals('unicode', type(string).__name__ )

    def test_endsWith(self):
        """
        Return True if the string ends with the specified suffix, otherwise return False. 
        suffix can also be a tuple of suffixes to look for. With optional start, test 
        beginning at that position. With optional end, stop comparing at that position.
        """
        string = 'test_end'
        self.assertTrue( string.endswith('_end') )
        self.assertFalse( string.endswith('test_') )

    def test_expandTabs(self):
        """
        Return a copy of the string where all tab characters are replaced by one or 
        more spaces, depending on the current column and the given tab size. 
        The column number is reset to zero after each newline occurring in the string. 
        If tabsize is not given, a tab size of 8 characters is assumed. This doesn’t 
        understand other non-printing characters or escape sequences.
        """
        string = 'teste\tteste\t'
        self.assertEquals('teste   teste   ', string.expandtabs() )

    def test_find(self):
        """
        Return the lowest index in the string where substring sub is found, such that 
        sub is contained in the slice s[start:end]. Optional arguments start and end 
        are interpreted as in slice notation. Return -1 if sub is not found.
        """
        string = "abcdefg" 
        self.assertEquals(3, string.find('d') )
        self.assertEquals(0, string.find('a') )
        self.assertEquals(6, string.find('g') )

    def test_fotmat(self):
        """
        Perform a string formatting operation. The string on which this 
        method is called can contain literal text or replacement fields 
        delimited by braces {}. Each replacement field contains either the 
        numeric index of a positional argument, or the name of a keyword argument. 
        Returns a copy of the string where each replacement field is replaced 
        with the string value of the corresponding argument.
        """
        self.assertEquals('[1, 2, 3]', "[{0}, {1}, {2}]".format(1, 2, 3) )
        self.assertEquals('[1, 1, 3]', "[{0}, {0}, {2}]".format(1, 2, 3) )
        
    def test_index(self):
        """
        Like find(), but raise ValueError when the substring is not found.
        """
        self.assertEquals(4, 'abcde'.index('e') )
        self.assertEquals(0, 'abcde'.index('a') )
        
    def test_isAlnum(self):
        """
        Return true if all characters in the string are alphanumeric and 
        there is at least one character, false otherwise.
        """
        self.assertFalse( '$%ss#@'.isalnum() )
        self.assertTrue( 'abcde'.isalnum() )

    def test_isAlpha(self):
        """
        Return true if all characters in the string are alphabetic and 
        there is at least one character, false otherwise.
        """
        self.assertTrue( 'abcd'.isalpha() )
        self.assertFalse( 'abcd.$%%'.isalpha() ) 

    def test_isDigit(self):
        """
        Return true if all characters in the string are digits and there is 
        at least one character, false otherwise.
        """
        self.assertTrue( '1234'.isdigit() )   
        self.assertFalse( 'a1234'.isdigit() )      

    def test_isLower(self):
        """
        Return true if all cased characters [4] in the string are lowercase 
        and there is at least one cased character, false otherwise.
        """
        self.assertTrue( 'a'.islower() )
        self.assertFalse( 'A'.islower() )

    def test_isSpace(self):
        """
        Return true if there are only whitespace characters in the string and 
        there is at least one character, false otherwise.
        """
        self.assertTrue( '  '.isspace() )
        self.assertFalse( ' .... '.isspace() )

    def test_lStrip(self):
        """
        Return a copy of the string with leading characters removed. The chars 
        argument is a string specifying the set of characters to be removed. 
        If omitted or None, the chars argument defaults to removing whitespace. 
        The chars argument is not a prefix; rather, all combinations of 
        its values are stripped:
        """
        string = '= Text of test ='
        value_expected = ' Text of test ='
        self.assertEquals(value_expected,  string.lstrip('=') )

    def test_partition(self):
        """
        Split the string at the first occurrence of sep, and return a 3-tuple 
        containing the part before the separator, the separator itself, and the 
        part after the separator. If the separator is not found, return a 3-tuple 
        containing the string itself, followed by two empty strings.
        """
        string = 'aaa,bbb,ccc'
        value_expected = ('aaa', ',', 'bbb,ccc')
        self.assertTupleEqual(value_expected, string.partition(','))

if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(StringTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

