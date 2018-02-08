#!/usr/bin/env python

################################################################################
# "SAAVpedia Library"
# Copyright (C) 2018 Young-Mook Kang <ymkang@thylove.org>
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

import os
import sqlite3

class SQLite3(object) :

    def __init__(self):
        theBasePath = os.path.dirname(os.path.realpath(__file__))
        theDBFilePath = theBasePath + '/saavpedia.db'
        if os.path.exists(theDBFilePath) and os.path.isfile(theDBFilePath):
            self.__itsConnection = sqlite3.connect(theDBFilePath)
            self.__itsCursor = self.__itsConnection.cursor()
        else:
            self.__itsCursor = None
            print 'There is no a SAAVpedia DB file in the SAAVpedia library folder.'

        #self.__itsQueryInput = SAAVpediaInput()
        #print(os.path.dirname(os.path.realpath(__file__)))
        pass

    def open(self, theDBFilePath):
        self.__itsConnection = sqlite3.connect(theDBFilePath)
        self.__itsCursor = self.__itsConnection.cursor()
        pass

    def close(self):
        self.__itsCursor.close()
        self.__itsCursor = None
        pass

    def execute(self, theCommand):
        if not self.__itsCursor == None:
            return self.__itsCursor.execute(theCommand)
        return None


if __name__ == '__main__':
    pass

