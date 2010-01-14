# -*- coding: utf8 -*-
"""finds hashes or mentionings"""

import unittest
import re
from string import punctuation

def find_hash(s, find_mentionings=False):
    """returns list of all hashes lowercase converted to unicode
    or mentioning if find_mentionings=True
    strip the first symbol"""

    if find_mentionings:
        hs = re.findall(r'@[^\s.\']+',s)
    else:
        hs = re.findall(r'#[^\s.\']+',s)

    for i in range(len(hs)):
        # convert all strings to unicode
        if isinstance(hs[i],str):
            hs[i] = unicode(hs[i],'utf8')
        hs[i] = hs[i].strip(punctuation)
        hs[i] = unicode.lower(hs[i])
    return hs


class FindHashTest(unittest.TestCase):

    def setUp(self):
        self.a = 'asdf sasf s #followfriday adf'
        self.b = 'asdf sasf s #followfriday'
        self.c = 'asdf sasf s #followfriday #ff #donetsk'
        self.d = '#140Conf'
        self.e = u'#ДФСА'
        self.f = u''
        self.g = u'афас сф асфдас '

    def test_length(self):
        'test lenght of hash lists returned'
        self.failUnless(len(find_hash(self.a)) == 1)
        self.failUnless(len(find_hash(self.b)) == 1)
        self.failUnless(len(find_hash(self.c)) == 3)

    def test_specific_hashes(self):
        'test that specific hashes are in result'
        self.failUnless('followfriday' in find_hash(self.a))
        self.failUnless('ff' in find_hash(self.c))
        self.failUnless('donetsk' in find_hash(self.c))
        self.failUnless(u'дфса' in find_hash(self.e))

    def test_lower(self):
        'test that case of all hashes is lowered'
        self.failUnless('140conf' in find_hash(self.d))
        self.failUnless(u'дфса' in find_hash(self.e))

    def test_empty(self):
        'test that string with no has returns nothing'
        self.failUnless(len(find_hash(self.f)) == 0)
        self.failUnless(len(find_hash(self.g)) == 0)

    def test_punctuation(self):
        'test punctuation stripping'
        self.failIf('140conf:' in find_hash('#140conf:'))
        self.failUnless('140conf' in find_hash('#140conf:'))

    def test_dot_inside(self):
        'test case #zimbabwe.already'
        self.failIf('zimbabwe.already' in find_hash('#zimbabwe.already'))
        self.failUnless('zimbabwe' in find_hash('#zimbabwe.already'))

    def test_find_person(self):
        'test that it finds people'
        self.failUnless('test' in find_hash('user @test',find_mentionings=True))
        self.failUnless('user2' in find_hash('user @test @user2',find_mentionings=True))
        self.failIf('user2' in find_hash('user @test #user2',find_mentionings=True))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
