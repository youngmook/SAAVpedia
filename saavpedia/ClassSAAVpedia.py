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

import requests
import uuid, time
from datetime import datetime
from ClassSAAVpediaInput import SAAVpediaInput

class SAAVpedia(object) :
    def __init__(self):
        self.__itsUrl = 'https://www.saavpedia.org/assets/lib/scripts/annotation.php'
        self.__itsDatasetName = datetime.now().strftime("%Y%m%d-%Hh%Mm%S.%f")[:-3] + 's-' + str(uuid.uuid4())[:8]
        self.__itsQueryInput = SAAVpediaInput()
        pass

    @property
    def url(self):
        return self.__itsUrl

    @url.setter
    def url(self, theValue):
        print "[{0}] Read only error, You can't change the URL!".format(theValue)
        pass

    @property
    def datasetName(self):
        return self.__itsDatasetName

    @datasetName.setter
    def datasetName(self, theName):
        if(type(str()) == type(theName)):
            self.__itsDatasetName = theName
            pass
        pass

    @property
    def input(self):
        return self.__itsQueryInput

    @input.setter
    def input(self, theSAAVpediaInput):
        if(type(theSAAVpediaInput) == type(SAAVpediaInput())):
            self.__itsQueryInput = theSAAVpediaInput
        else:
            raise "SAAVpedia query input is wrong!"
        pass



if __name__ == '__main__':

    s = SAAVpedia()

    s.input.genomicPosition = '100'
    s.input.unitprot = 'NX-1010'

    print s.input.genomicPosition
    print s.input.unitprot
    print s.input.nextprot



    pass


