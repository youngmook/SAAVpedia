#!/usr/bin/env python

################################################################################
# "SAAVpedia Annotation Javascript Library"
# Copyright (C) 2017 Young-Mook Kang <ymkang@thylove.org>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
################################################################################

import unittest
from saavpedia import SAAVpediaInput

class SAAVpediaInputTest(unittest.TestCase):

    def setUp(self):
        self.input = SAAVpediaInput()
        pass

    def tearDown(self):
        pass

    def test_ENSP(self):
        self.input.ENSP = 'ENSP00000000233'
        self.assertEqual(type(str()), type(self.input.ENSP))
        self.assertEqual('ENSP00000000233', self.input.ENSP)
        self.assertEqual('ENSP00000000233', self.input.ensp)
        pass

    def test_ENSG(self):
        self.input.ENSG = 'ENSG00000000233'
        self.assertEqual(type(str()), type(self.input.ENSG))
        self.assertEqual('ENSG00000000233', self.input.ENSG)
        self.assertEqual('ENSG00000000233', self.input.ensg)
        pass

    def test_ENST(self):
        self.input.ENST = 'ENSG00000000233'
        self.assertEqual(type(str()), type(self.input.ENST))
        self.assertEqual('ENSG00000000233', self.input.ENST)
        self.assertEqual('ENSG00000000233', self.input.enst)
        pass

    def testCosmic(self):
        self.input.cosmic = 'COSMIC'
        self.assertEqual(type(str()), type(self.input.cosmic))
        self.assertEqual('COSMIC', self.input.cosmic)
        pass

    def testDbSNP(self):
        self.input.dbSNP = 'dbSNP'
        self.assertEqual(type(str()), type(self.input.dbSNP))
        self.assertEqual('dbSNP', self.input.dbSNP)
        pass

    def testDbSNP(self):
        self.input.dbSNP = 'dbSNP'
        self.assertEqual(type(str()), type(self.input.dbSNP))
        self.assertEqual('dbSNP', self.input.dbSNP)
        pass

    def testSAAVPepSeq(self):
        theTestInput = 'LEAK'
        self.input.saavPeptideSequence = theTestInput
        self.assertEqual(type(str()), type(self.input.saavPeptideSequence))
        self.assertEqual(theTestInput, self.input.saavPeptideSequence)
        pass

    def testGenomicPosition(self):
        theTestInput = '10000'
        self.input.genomicPosition = theTestInput
        self.assertEqual(type(str()), type(self.input.genomicPosition))
        self.assertEqual(theTestInput, self.input.genomicPosition)






if __name__ == '__main__':
    unittest.main()
