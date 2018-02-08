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

import re

class SAAVpediaInputParser(object):
    def __init__(self):
        self.__its2dStringData = []
        self.__itsColOfRsID           = 'col6'
        self.__itsColOfCosmicID       = 'col6'
        self.__itsColOfENSP           = 'col43'
        self.__itsColOfENST           = 'col10'
        self.__itsColOfENSG           = 'col9'
        self.__itsColOfSAAVpeptideSeq = 'col14'
        self.__itsColOfUniprot        = 'col8'
        self.__itsColOfNextprot       = 'col7'

        self.__itsUniprotMatcher = re.compile( \
            '[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}')
        pass

    def __aListToSqlString(self, theStringList):
        theList = []
        for i in theStringList:
            theList.append(self.__stringToQuery(i))
        return "("+" AND ".join(theList)+")"

    def __2dListToSqlString(self, the2dList):
        theQueryList = []
        for ithList in the2dList:
            theQueryList.append(self.__aListToSqlString(ithList))
            pass
        return "("+" OR ".join(theQueryList)+")"


    def __aListToQueryDict(self, theStringList):
        theQueryDict = {}
        for i in theStringList:
            self.__addQueryToQueryDict(theQueryDict, i)
        return theQueryDict

    def __2dListToQueryDictList(self, the2dList):
        theQueryDictList = []
        for ithList in the2dList:
            theQueryDictList.append(self.__aListToQueryDict(ithList))
            pass
        return theQueryDictList

    def __isDigitIncludingPrefix(self, theString, thePrefix):
        if (len(theString) < len(thePrefix)) :
            return False
        if not (thePrefix.upper() == str(theString[:len(thePrefix)]).upper()):
            return False
        if (str(theString[len(thePrefix):]).isdigit()):
            return True
        return False

    def __isENSP(self, theString):
        return self.__isDigitIncludingPrefix(theString, 'ENSP')

    def __isENST(self, theString):
        return self.__isDigitIncludingPrefix(theString, 'ENST')

    def __isENSG(self, theString):
        return self.__isDigitIncludingPrefix(theString, 'ENSG')

    def __isRsID(self, theString):
        return self.__isDigitIncludingPrefix(theString, 'rs')

    def __isCosmicID(self, theString):
        return self.__isDigitIncludingPrefix(theString, 'COSM')

    def __isUniprot(self, theString):
        return bool(self.__itsUniprotMatcher.match(theString))

    def __isNextprot(self, theString):
        thePrefix = 'NX_'
        if len(theString) < len(thePrefix):
            return False
        theTail = theString[len(thePrefix):].split('-')[0]
        return bool(self.__itsUniprotMatcher.match(theTail))


    def __stringToQuery(self, theString):
        if self.__isCosmicID(theString):
            return '({0} LIKE \"{1}\")'.format(self.__itsColOfCosmicID, theString.upper())
        elif self.__isRsID(theString):
            return '({0} LIKE \"{1}\")'.format(self.__itsColOfRsID, theString.lower())
        elif self.__isENSG(theString):
            return '({0} LIKE \"{1}\")'.format(self.__itsColOfENSG, theString.upper())
        elif self.__isENST(theString):
            return '({0} LIKE \"{1}\")'.format(self.__itsColOfENST, theString.upper())
        elif self.__isENSP(theString):
            return '({0} LIKE \"{1}\")'.format(self.__itsColOfENSP, theString.upper())
        elif self.__isUniprot(theString):
            return '({0} LIKE \"{1}\")'.format(self.__itsColOfUniprot, theString.upper())
        elif self.__isNextprot(theString):
            return '({0} LIKE \"{1}\")'.format(self.__itsColOfNextprot, theString.upper())
        elif str(theString).isalpha():
            return '({0} LIKE \"{1}\")'.format(self.__itsColOfSAAVpeptideSeq, theString.upper())

    def __addQueryToQueryDict(self, theQueryDict, theString):
        theKey = None
        if self.__isCosmicID(theString):
            theKey = 'cosmic'
        elif self.__isRsID(theString):
            theKey = 'rs'
        elif self.__isENSG(theString):
            theKey = 'ensg'
        elif self.__isENST(theString):
            theKey = 'enst'
        elif self.__isENSP(theString):
            theKey = 'ensp'
        elif self.__isUniprot(theString):
            theKey = 'uniprot'
        elif self.__isNextprot(theString):
            theKey = 'nextprot'
        elif str(theString).isalpha():
            theKey = 'seq'
        if theKey != None:
            if theQueryDict.has_key(theKey):
                if type(theQueryDict[theKey]) == type(list()):
                    theSet = set(theQueryDict[theKey])
                    theSet.add(theString)
                    theQueryDict[theKey] = list(theSet)
                else:
                    theSet = set([theQueryDict[theKey], theString])
                    theQueryDict[theKey] = list(theSet)
            else :
                theQueryDict[theKey] = theString

    def toSqlCondition(self):
        return self.__2dListToSqlString(self.__its2dStringData)

    def __str__(self):
        return self.toString()

    def toQueryList(self):
        return self.__2dListToQueryDictList(self.__its2dStringData)

    def toString(self):
        return str(self.toQueryList())

    def setupToSAAVIdentifier(self):
        theQueryDictList = self.__2dListToQueryDictList(self.__its2dStringData)
        theString = ""
        for ithDict in theQueryDictList:
            if ithDict.has_key('seq'):
                theString += ithDict['seq'] + '\n'
                pass
            pass
        self.set(theString)
        pass

    def setupToSNVRetrieval(self):
        theQueryDictList = self.__2dListToQueryDictList(self.__its2dStringData)
        theString = ""
        for ithDict in theQueryDictList:
            if ithDict.has_key('cosmic'):
                theString += str(ithDict['cosmic']).upper() + '\t'
                pass
            if ithDict.has_key('rs'):
                theString += str(ithDict['rs']).lower() + '\t'
                pass
            theString += '\n'
            pass
        self.set(theString)
        pass

    def setupToBiomoleculeRetrieval(self):
        theQueryDictList = self.__2dListToQueryDictList(self.__its2dStringData)
        theString = ""
        for ithDict in theQueryDictList:
            if ithDict.has_key('ensg'):
                theString += str(ithDict['ensg']).upper() + '\t'
                pass
            if ithDict.has_key('enst'):
                theString += str(ithDict['enst']).upper() + '\t'
                pass
            if ithDict.has_key('ensp'):
                theString += str(ithDict['ensp']).upper() + '\t'
                pass
            if ithDict.has_key('uniprot'):
                theString += str(ithDict['uniprot']).upper() + '\t'
                pass
            if ithDict.has_key('nextprot'):
                theString += str(ithDict['nextprot']).upper() + '\t'
                pass
            theString += '\n'
            pass
        self.set(theString)
        pass

    def set(self, theStringInput):
        the2dStringData = []
        theSplitedLineList = theStringInput.replace('\r','').strip().split('\n')
        for ithLine in theSplitedLineList:
            the2dStringData.append(ithLine.split())
            pass
        self.__its2dStringData = the2dStringData
        pass
    pass



if __name__ == '__main__':
    theInput = "NDVDCAYLR\nWLEAK\tQ7Z5L2\tNX_Q7Z5L2-3\nPLEAK\t\tQ7Z5L2\tNX_Q7Z5L2-3 ENSG00000166024\nNX_Q7Z5L2-3 ENSG00000166024\nRS1049550\nCOSM4418633"
    parser = SAAVpediaInputParser()
    parser.set(theInput)
    print parser.toSqlCondition()

    parser.setupToSAAVIdentifier()
    print parser.toSqlCondition()

    parser.set(theInput)
    parser.setupToSNVRetrieval()
    print parser.toSqlCondition()

    parser.set(theInput)
    parser.setupToBiomoleculeRetrieval()
    print parser.toSqlCondition()

    pass


