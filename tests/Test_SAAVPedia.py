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
from saavpedia import SAAVpedia

class SAAVpediaTest(unittest.TestCase):

    def setUp(self):
        self.saavpedia = SAAVpedia()
        pass

    def tearDown(self):
        pass

    def test_url(self):
        self.assertEqual(type(str()), type(self.saavpedia.url))

if __name__ == '__main__':
    unittest.main()
