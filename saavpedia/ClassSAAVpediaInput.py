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

class SAAVpediaInput(object) :
    def __init__(self):
        self.__itsQueryOfSAAVpeptideSequence = None
        self.__itsQueryOfENSP                = None
        self.__itsQueryOfENST                = None
        self.__itsQueryOfENSG                = None
        self.__itsQueryOfUnitprot            = None
        self.__itsQueryOfNextprot            = None
        self.__itsQueryOfGenomicPosition     = None
        self.__itsQueryOfdbSNP               = None
        self.__itsQueryOfCosmic              = None

        pass


    ################################################################################
    # ENSP input
    ################################################################################
    @property
    def ENSP(self):
        return self.__itsQueryOfENSP

    @ENSP.setter
    def ENSP(self, theENSP):
        self.__itsQueryOfENSP = str(theENSP)
        pass

    @property
    def ensp(self):
        return self.ENSP

    @ensp.setter
    def ensp(self, theENSP):
        self.ENSP = theENSP
        pass

    ################################################################################
    # ENST input
    ################################################################################
    @property
    def ENST(self):
        return self.__itsQueryOfENST

    @ENST.setter
    def ENST(self, theENST):
        self.__itsQueryOfENST = str(theENST)
        pass

    @property
    def enst(self):
        return self.ENST

    @enst.setter
    def enst(self, theENST):
        self.ENST = theENST
        pass

    ################################################################################
    # ENSG input
    ################################################################################
    @property
    def ENSG(self):
        return self.__itsQueryOfENSG

    @ENSG.setter
    def ENSG(self, theENSG):
        self.__itsQueryOfENSG = str(theENSG)
        pass

    @property
    def ensg(self):
        return self.ENSG

    @ensg.setter
    def ensg(self, theENSG):
        self.ENSG = theENSG
        pass

    ################################################################################
    # Uniprot input
    ################################################################################
    @property
    def unitprot(self):
        return self.__itsQueryOfUnitprot

    @unitprot.setter
    def unitprot(self, theUnitprotID):
        self.__itsQueryOfUnitprot = str(theUnitprotID)
        pass

    ################################################################################
    # Nextprot input
    ################################################################################
    @property
    def nextprot(self):
        return self.__itsQueryOfNextprot

    @nextprot.setter
    def nextprot(self, theNextprotID):
        self.__itsQueryOfNextprot = str(theNextprotID)
        pass

    ################################################################################
    # SAAV peptide sequence input
    ################################################################################
    @property
    def saavPeptideSequence(self):
        return self.__itsQueryOfSAAVpeptideSequence

    @saavPeptideSequence.setter
    def saavPeptideSequence(self, theNextprotID):
        self.__itsQueryOfSAAVpeptideSequence = str(theNextprotID)
        pass

    ################################################################################
    # dbSNP input
    ################################################################################
    @property
    def dbSNP(self):
        return self.__itsQueryOfdbSNP

    @dbSNP.setter
    def dbSNP(self, theDbSNP):
        self.__itsQueryOfdbSNP = str(theDbSNP)
        pass

    ################################################################################
    # Cosmic input
    ################################################################################
    @property
    def cosmic(self):
        return self.__itsQueryOfCosmic

    @cosmic.setter
    def cosmic(self, theCosmicID):
        self.__itsQueryOfCosmic = str(theCosmicID)
        pass


    ################################################################################
    # Genomic position input
    ################################################################################
    @property
    def genomicPosition(self):
        return self.__itsQueryOfGenomicPosition

    @genomicPosition.setter
    def genomicPosition(self, thePosition):
        self.__itsQueryOfGenomicPosition = str(thePosition)
        pass

    def __isNone(self, theObject):
        if(type(None) == type(theObject)):
            return True
        return False

    def __isNotNone(self, theObject):
        if (type(None) != type(theObject)):
            return True
        return False


    def __arrayToQueryRequest(self, theValueList):
        pass

    def toString(self):
        theString = ''
        if self.__isNotNone(self.saavPeptideSequence) :
            theString = theString + 'saav_pep_seq='


        '''
                self.__itsQueryOfSAAVpeptideSequence = None
        self.__itsQueryOfENSP                = None
        self.__itsQueryOfENST                = None
        self.__itsQueryOfENSG                = None
        self.__itsQueryOfUnitprot            = None
        self.__itsQueryOfNextprot            = None
        self.__itsQueryOfGenomicPosition     = None
        self.__itsQueryOfdbSNP               = None
        self.__itsQueryOfCosmic              = None
        :return: 
        '''

    def __str__(self):
        return self.toString()


if __name__ == '__main__':
    pass


